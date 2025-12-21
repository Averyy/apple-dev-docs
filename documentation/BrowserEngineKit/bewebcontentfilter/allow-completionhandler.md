# allow(_:completionHandler:)

**Framework**: BrowserEngineKit  
**Kind**: method

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
func allow(_ url: URL) async throws -> Bool
```

#### Discussion

Adds blocked URL to built-in web content filter’s allowlist.

## Parameters

- `url`: The URL to be added.
- `completionHandler`: The completion block to be called when the add   operation is complete, with result of the operation. Result is YES if the url is added   successfully, and NO if it isn’t.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bewebcontentfilter/allow(_:completionhandler:))*