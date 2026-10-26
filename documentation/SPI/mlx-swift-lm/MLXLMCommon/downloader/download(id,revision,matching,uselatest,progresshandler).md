---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/downloader/download(id:revision:matching:uselatest:progresshandler:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# download(id:revision:matching:useLatest:progressHandler:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Download (or retrieve from cache) a snapshot of a repository.

## Declaration

```swift
func download(id: String, revision: String?, matching patterns: [String], useLatest: Bool, progressHandler: @Sendable @escaping (Progress) -> Void) async throws -> URL
```

#### Return Value

Local directory URL containing the downloaded files

## Parameters

- `id`: Provider-specific repository identifier
- `revision`: Optional revision (branch, tag, commit hash, version number). Providers without versioning receive `nil`.
- `patterns`: Glob patterns to filter which files to download (e.g. `["*.safetensors", "*.json", "*.jinja"]`)
- `useLatest`: When `true`, check the provider for updates even if a cached version exists. When `false`, return the cached version if available.
- `progressHandler`: Callback for download progress


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/downloader/download(id:revision:matching:uselatest:progresshandler:))*