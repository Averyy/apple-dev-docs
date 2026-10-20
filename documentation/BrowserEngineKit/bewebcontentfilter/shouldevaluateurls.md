# shouldEvaluateURLs

**Framework**: BrowserEngineKit  
**Kind**: property  
**Role**: Type Property

Determines whether the built-in web content filter is active.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
class var shouldEvaluateURLs: Bool { get }
```

```objc
@property (class, readonly) BOOL shouldEvaluateURLs;
```

#### Return Value

`true` if the built-in web content filter is active; `false`, otherwise.

## See Also

### Evaluating URLs
- [func evaluateURL(URL, completionHandler: (Bool, Data?) -> Void)](./evaluateurl%28_,completionhandler%29.md)
  Determines whether to block a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bewebcontentfilter/shouldevaluateurls)*