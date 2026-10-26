---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/using"
framework: "mlx-swift-lm/MLXLMCommon"
---

# Using mlx-swift-lm

**Framework**: mlx-swift-lm/MLXLMCommon  
**Role**: Article

How to use mlx-swift-lm in your own tools and applications

#### Overview

Using mlx-swift-lm to add LLM, VLM or text embedding capabilities to your own software is straightforward:

- add a depdendency on `mlx-swift-lm`
- add a dependency on a *Downloader* and *Tokenizer*
- adapt the API of the Downloader and Tokenizer to conform to the protocols

Then make use of the model:

```swift
import MLXLMCommon
    
let downloader: any Downloader = ...
let tokenizerLoader: any TokenizerLoader = ...

let model = try await loadModel(
    from: downloader,
    using: tokenizerLoader,
    id: "mlx-community/Qwen3-4B-4bit"
)
let session = ChatSession(model)
print(try await session.respond(to: "What are two things to see in San Francisco?"))
print(try await session.respond(to: "How about a great place to eat?"))
```

#### Downloaders and Tokenizers

There are 3 general ways to select and use concrete Downloader and Tokenizer implementations:

- implementing protocols
- using an integration package
- using [MLXHuggingFace](./mlxhuggingface.md) macros

If you are [Upgrade From 2.x Release](./upgrade.md) from mlx-swift-lm 2.x the macros will be the simplest way, but consider [Integration Packages](./using.md#Integration-Packages) as there are alternate implementations that may provide features and capabilities that you want.

##### Implementing Protocols

The other two methods use exactly this technique to wrap concrete implementations in the mlx-swift-lm protocol.  You can do this yourself if you have custom code or simply wish to see how it works.

mlx-swift-lm requires implementation of at least the two tokenizer protocols:

- [`Downloader`](./downloader.md) – required if you need to download weights.  Not needed if you have local weights.
- [`Tokenizer`](./tokenizer.md) – adapt the concrete tokenizers to the mlx-swift-lm protocol.
- [`TokenizerLoader`](./tokenizerloader.md) – factory for [`Tokenizer`](./tokenizer.md) implementations.

You can look at [Integration Packages](./using.md#Integration-Packages) implementations for examples of how to write these – there are only a few properties and methods and they typically have trivial mappings to the concrete implementation.

A tokenizer can override [`makeStreamingDetokenizer()`](./tokenizer/makestreamingdetokenizer%28%29.md) to provide its own incremental decoder. The default returns [`NaiveStreamingDetokenizer`](./naivestreamingdetokenizer.md). Each call must create independent state and preserve special tokens used by tool and reasoning parsers. Emit only stable text from `next()`; return any remaining text from [`finish()`](./streamingdetokenizer/finish%28%29.md). Generation flushes the decoder before finishing downstream parsers, and framed protocols start a fresh decoder for each payload. A consumer that stops early can discard the remaining state.

This example shows adapting `HuggingFace.HubClient` to the `Downloader` protocol:

```swift
import HuggingFace
import MLXLMCommon

struct HubDownloader: MLXLMCommon.Downloader {
    private let upstream: HubClient

    init(_ upstream: HubClient) {
        self.upstream = upstream
    }
    
    init() {
        self.upstream = HubClient()
    }

    public func download(
        id: String,
        revision: String?,
        matching patterns: [String],
        useLatest: Bool,
        progressHandler: @Sendable @escaping (Progress) -> Void
    ) async throws -> URL {                        
        guard let repoID = HuggingFace.Repo.ID(rawValue: id) else {
            throw HuggingFaceDownloaderError.invalidRepositoryID(id)
        }
        let revision = revision ?? "main"

        return try await upstream.downloadSnapshot(
            of: repoID,
            revision: revision,
            matching: patterns,
            progressHandler: { @MainActor progress in
                progressHandler(progress)
            }
        )
    }                    
}

// now you can use it
let downloader = HubDownloader()
let tokenizerLoader: any TokenizerLoader = ...

let model = try await loadModel(
    from: downloader,
    using: tokenizerLoader,
    id: "mlx-community/Qwen3-4B-4bit"
)
```

##### Integration Packages

Integration packages provide an adapter that encapsulates a concrete implementation.  Adding a dependency on the adapter will transitively add a dependency on the implementation.

So which adapter do you chose?

- `huggingface/swift-transformers`

  - this is the package that mlx-swift-lm originally integrated with

No additional integration packages are provided at this time, but feel free to contribute one!

See [Xcode projects](./using.md#Xcode-projects) for information about how to hook it up.

##### MLXHuggingFace Macros

To provide parity with mlx-swift-lm 2.x there is a built in integration with the HuggingFace downloader and tokenizer implementations using macros.

Add these dependencies to your project (see [Xcode projects](./using.md#Xcode-projects)):

- [https://github.com/huggingface/swift-huggingface](https://github.com/huggingface/swift-huggingface)
- [https://github.com/huggingface/swift-transformers](https://github.com/huggingface/swift-transformers)

and add `HuggingFace`, `Tokenizers`, `MLXLLM`, `MLXLMCommon` and `MLXHuggingFace` as libraries that your project links.

You can use the integration like this:

```swift
import MLXLLM
import MLXLMCommon
import MLXHuggingFace

import HuggingFace
import Tokenizers

let modelConfiguration = LLMRegistry.gemma3_1B_qat_4bit

let model = try await #huggingFaceLoadModelContainer(
    configuration: modelConfiguration
)

let session = ChatSession(model)
print(try await session.respond(to: "What are two things to see in San Francisco?"))
print(try await session.respond(to: "How about a great place to eat?"))
```

or if you prefer more explicit downloader and tokenizer loading for more control:

```swift
import HuggingFace
import Tokenizers

import MLXLLM
import MLXLMCommon
import MLXHuggingFace

let modelConfiguration = LLMRegistry.gemma3_1B_qat_4bit

let model = try await LLMModelFactory.shared.loadContainer(
    from: #hubDownloader(),
    using: #huggingFaceTokenizerLoader(),
    configuration: modelConfiguration
)

let session = ChatSession(model)
print(try await session.respond(to: "What are two things to see in San Francisco?"))
print(try await session.respond(to: "How about a great place to eat?"))
```

`#hubDownloader()` provides an integration just like what is shown in [Implementing Protocols](./using.md#Implementing-Protocols) and `#huggingFaceTokenizerLoader()` provides something similar to load the tokenizers.

See [Upgrade From 2.x Release](./upgrade.md) for more information on upgrading from a 2.x release.

#### Xcode projects

You can read the [Xcode documentation](https://developer.apple.com/documentation/xcode/adding-package-dependencies-to-your-app).

Click on your project (the top item in the Xcode navigator) and select the **Project** (top item).  Then select **Package Dependencies** and click `+` to add a new dependency.

For all integration methods you will need to add:

- [https://github.com/ml-explore/mlx-swift-lm](https://github.com/ml-explore/mlx-swift-lm)

Beyond that, chose one of the 3 integration methods and add either the adapter packages OR the implementation packages if using macros/local implemenentation.  See <doc#Integration-Packages>.

#### Package.swift / SwiftPM

In your Package.swift add a reference to mlx-swift-lm, chosing either the `main` branch or something that tracks versions:

```swift
.package(url: "https://github.com/ml-explore/mlx-swift-lm", .upToNextMinor(from: "3.32.3")),
```

Beyond that, chose one of the 3 integration methods and add either the adapter packages OR the implementation packages if using macros/local implemenentation.  See <doc#Integration-Packages>.

You can use the [MLXHuggingFace Macros](./using.md#MLXHuggingFace-Macros) like this:

```swift
.package(url: "https://github.com/huggingface/swift-huggingface", from: "0.9.0"),
.package(url: "https://github.com/huggingface/swift-transformers", from: "1.3.0"),
```

```swift
.target(
    name: "YourTargetName",
    dependencies: [
        .product(name: "MLXLLM", package: "mlx-swift-lm"),
        .product(name: "MLXHuggingFace", package: "mlx-swift-lm"),
        .product(name: "HuggingFace", package: "swift-huggingface"),
        .product(name: "Tokenizers", package: "swift-transformers"),
    ]),
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/using)*