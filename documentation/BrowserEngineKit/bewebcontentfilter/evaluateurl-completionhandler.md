# evaluateURL(_:completionHandler:)

**Framework**: BrowserEngineKit  
**Kind**: method

Determines whether to block a URL.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
func evaluateURL(_ url: URL) async -> (Bool, Data?)
```

#### Discussion

If this method blocks a URL, it returns a UTF-8 encoded HTML representation of a blocking page.

This method performs a lazy initialization of some objects, so the first call can take longer than subsequent calls.

## Parameters

- `url`: The URL to evaluate.
- `completionHandler`: A closure that the system invokes when URL evaluation finishes. The closure returns `true` if the URL is blocked; `false`, otherwise.

## See Also

- [class var shouldEvaluateURLs: Bool](bewebcontentfilter/shouldevaluateurls.md)
  Determines whether the built-in web content filter is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bewebcontentfilter/evaluateurl(_:completionhandler:))*