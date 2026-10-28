# evaluateURL(_:completionHandler:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Determines whether to block a URL.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
func evaluateURL(_ url: URL, completionHandler: @escaping @Sendable (Bool, Data?) -> Void)
```

```swift
func evaluateURL(_ url: URL) async -> (Bool, Data?)
```

```objc
- (void) evaluateURL:(NSURL *) url completionHandler:(void (^)(BOOL shouldBlock, NSData *blockPageRepresentation)) completionHandler;
```

## Discussion

If this method blocks a URL, it returns a UTF-8 encoded HTML representation of a blocking page.

This method performs a lazy initialization of some objects, so the first call can take longer than subsequent calls.

## Parameters

- `url`: The URL to evaluate.
- `completionHandler`: A closure that the system invokes when URL evaluation finishes. The closure returns `true` if the URL is blocked; `false`, otherwise.

## See Also

### Evaluating URLs
- [class var shouldEvaluateURLs: Bool](./shouldevaluateurls.md)
  Determines whether the built-in web content filter is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bewebcontentfilter/evaluateurl(_:completionhandler:))*