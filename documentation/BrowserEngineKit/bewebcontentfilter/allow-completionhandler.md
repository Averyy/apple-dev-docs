# allow(_:completionHandler:)

**Framework**: BrowserEngineKit  
**Kind**: method

Adds a previously blocked URL to the web content filter’s allow list.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
func allow(_ url: URL) async throws -> Bool
```

## Parameters

- `url`: The URL to unblock.
- `completionHandler`: A closure that the system invokes when the add operation finishes. The closure returns `true` on success; `false`, otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bewebcontentfilter/allow(_:completionhandler:))*