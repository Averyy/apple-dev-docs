---
url: "https://docs.swift.org/latest/documentation/wasmguide/concurrency"
framework: "Swift-Org/WasmGuide"
---

# Concurrency

**Framework**: Swift-Org/WasmGuide  
**Role**: Article

On macOS, iOS, and Linux, the `libdispatch`-based executor is used by default, but `libdispatch` is not supported in a single-threaded WebAssembly environment. However, there are still two global task executors available in Swift for Wasm.

## Overview

If you need multi-threading support, please see [Multithreading guide](./multithreading.md) for more details.

## Cooperative Task Executor

`Cooperative Task Executor` is the default task executor when targeting Wasm. It is a simple single-threaded cooperative task executor implemented in [Swift Concurrency library](https://github.com/swiftlang/swift/blob/0c67ce64874d83b2d4f8d73b899ee58f2a75527f/stdlib/public/Concurrency/CooperativeGlobalExecutor.inc). If you are not familiar with the term “Cooperative” in the context of concurrent programming, see [its definition for more details](https://en.wikipedia.org/wiki/Cooperative_multitasking).

This executor has an *event loop* that dispatches tasks until no more tasks are enqueued, and exits immediately after all tasks are dispatched. Note that this executor won’t yield control to the host environment during execution, so any host’s async operation cannot call back to the Wasm execution.

This executor is suitable for WASI command line tools, or host-independent standalone applications.

Here’s an example that you can run on CLI with `swift run --swift-sdk "$(swiftc -print-target-info | jq -r '.swiftCompilerTag')_wasm"`:

```swift
@main
struct Main {
    static func main() async throws {
        print("Sleeping for 1 second... 😴")
        try await Task.sleep(nanoseconds: 1_000_000_000)
        print("Wake up! 😁")
    }
}
```

## JavaScript Event Loop-based Task Executor

`JavaScript Event Loop-based Task Executor` is a task executor that cooperates with JavaScript’s event loop. It is provided by [JavaScriptKit](https://github.com/swiftwasm/JavaScriptKit), and you need to activate it explicitly by calling a predefined `JavaScriptEventLoop.installGlobalExecutor()` function (see below for more details).

This executor also has its own *event loop* that dispatches tasks until no more tasks are enqueued synchronously. It yields control to the JavaScript side after all pending tasks are dispatched, so the JavaScript program can call back to the executed Wasm module. After a task is resumed by callbacks from JavaScript, the executor starts its event loop again in the next microtask tick.

To enable this executor, you need to use the `JavaScriptEventLoop` module, which is provided as a part of `JavaScriptKit` package.

1. Ensure that you have added `JavaScriptKit` dependency to your `Package.swift`
2. Add `JavaScriptEventLoop` dependency to your targets that use this executor

```swift
.product(name: "JavaScriptEventLoop", package: "JavaScriptKit"),
```

1. Import `JavaScriptEventLoop` and call `JavaScriptEventLoop.installGlobalExecutor()` before spawning any tasks to activate the executor instead of the default cooperative executor.

This executor is only available on JavaScript host environment.

See also [JavaScriptKit documentation](https://github.com/swiftwasm/JavaScriptKit/#asyncawait) for more details.

```swift
import JavaScriptEventLoop
import JavaScriptKit

JavaScriptEventLoop.installGlobalExecutor()

let document = JSObject.global.document
var asyncButtonElement = document.createElement("button")
_ = document.body.appendChild(asyncButtonElement)

asyncButtonElement.innerText = "Fetch Zen"
func printZen() async throws {
    let fetch = JSObject.global.fetch.function!
    let response = try await JSPromise(fetch("https://api.github.com/zen").object!)!.value
    let text = try await JSPromise(response.text().object!)!.value
    print(text)
}
asyncButtonElement.onclick = .object(JSClosure { _ in
    Task {
        do {
            try await printZen()
        } catch {
            print(error)
        }
    }

    return .undefined
})
```

## See Also

- [Porting code from other platforms](./porting.md)
  Make your code cross-platform and compatible with WebAssembly by checking for libraries and APIs available for this platform.
- [Testing](./testing.md)
  Swift for WebAssembly supports both `swift-testing` and `XCTest` for writing test suites. Your project needs to have a `Package.swift` package manifest with test targets configured.
- [Debugging](./debugging.md)
  Debugging is a crucial part of the development process. With official toolchains providing more integrated tools, debugging WebAssembly modules has become more streamlined.
- [Troubleshooting](./troubleshooting.md)
  These are some common issues you may run into while using Swift with WebAssembly.
- [Importing and Exporting Functions](./importingexportingfunctions.md)
  WebAssembly modules often need to interact with their host environment. This guide demonstrates how to build a Swift guest module that both exports functions to the host and imports functions from it, using `WasmKit` as the host application.
- [Multi-threading](./multithreading.md)
  While Swift Concurrency is available in Swift for WebAssembly out of the box, it is single-threaded by default. Read this article for special considerations relevant to multi-threading.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/wasmguide/concurrency)*