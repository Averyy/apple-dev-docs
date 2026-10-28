# evaluateURL(_:completionHandler:)

**Framework**: BrowserKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
func evaluateURL(_ url: URL, completionHandler: @escaping @Sendable (Bool) -> Void)
```

```swift
func evaluateURL(_ url: URL) async -> Bool
```

```objc
- (void) evaluateURL:(NSURL *) url completionHandler:(void (^)(BOOL shouldBlock)) completionHandler;
```

## Discussion

Evaluates whether a URL should be blocked.

## Parameters

- `url`: The URL to be evaluated.
- `completionHandler`: The completion block to be invoked with result when evaluation is complete. Result is YES if the url should be blocked, and NO if it isn’t.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/bebrowsercontentfilter/evaluateurl(_:completionhandler:))*