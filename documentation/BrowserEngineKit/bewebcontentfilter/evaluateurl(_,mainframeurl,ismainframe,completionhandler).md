# evaluateURL(_:mainFrameURL:isMainFrame:completionHandler:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Determines whether to block a URL, using the main document’s URL as navigation context.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
func evaluateURL(_ url: URL, mainFrameURL: URL, isMainFrame: Bool, completionHandler: @escaping @Sendable (Bool, Data?) -> Void)
```

```swift
func evaluateURL(_ url: URL, mainFrameURL: URL, isMainFrame: Bool) async -> (Bool, Data?)
```

```objc
- (void) evaluateURL:(NSURL *) url mainFrameURL:(NSURL *) mainFrameURL isMainFrame:(BOOL) isMainFrame completionHandler:(void (^)(BOOL shouldBlock, NSData *blockPageRepresentation)) completionHandler;
```

## Discussion

If this method blocks a URL, it returns a UTF-8 encoded HTML representation of a blocking page to display in the blocked main document or subframe.

## Parameters

- `url`: The URL to evaluate, either a main frame or subframe URL.
- `mainFrameURL`: The URL of the main document. This may match `url` for main frame navigations.
- `isMainFrame`: `true` if `url` is a main frame navigation; `false` if it’s a subframe navigation.
- `completionHandler`: A closure that the system invokes when URL evaluation finishes. The closure returns `true` if the URL is blocked; `false`, otherwise.

## See Also

### Evaluating URLs
- [func evaluateURL(URL, completionHandler: (Bool, Data?) -> Void)](./evaluateurl%28_,completionhandler%29.md)
  Determines whether to block a URL.
- [class var shouldEvaluateURLs: Bool](./shouldevaluateurls.md)
  Determines whether the built-in web content filter is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bewebcontentfilter/evaluateurl(_:mainframeurl:ismainframe:completionhandler:))*