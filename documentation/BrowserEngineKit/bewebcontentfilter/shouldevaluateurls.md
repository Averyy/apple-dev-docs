# shouldEvaluateURLs

**Framework**: BrowserEngineKit  
**Kind**: property

Determines whether the built-in web content filter is active.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
class var shouldEvaluateURLs: Bool { get }
```

#### Return Value

`true` if the built-in web content filter is active; `false`, otherwise.

## See Also

- [func evaluateURL(URL, completionHandler: (Bool, Data?) -> Void)](bewebcontentfilter/evaluateurl(_:completionhandler:).md)
  Determines whether to block a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bewebcontentfilter/shouldevaluateurls)*