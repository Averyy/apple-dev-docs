# evaluateURL(_:completionHandler:)

**Framework**: BrowserEngineKit  
**Kind**: method

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
func evaluateURL(_ url: URL) async -> (Bool, Data?)
```

#### Discussion

Evaluates whether a URL should be blocked and if so, provides a UTF-8 encoded HTML representation of a blocking page.

This method performs a lazy initialization of some objects, so the first call could take longer than subsequent calls.

## Parameters

- `url`: The URL to be evaluated.
- `completionHandler`: The completion block to be invoked with result when   evaluation is complete. Result is YES if the url should be blocked, and NO if it isn’t.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bewebcontentfilter/evaluateurl(_:completionhandler:))*