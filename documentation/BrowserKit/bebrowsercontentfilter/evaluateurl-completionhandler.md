# evaluateURL(_:completionHandler:)

**Framework**: BrowserKit  
**Kind**: method

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
func evaluateURL(_ url: URL) async -> Bool
```

#### Discussion

Evaluates whether a URL should be blocked.

## Parameters

- `url`: The URL to be evaluated.
- `completionHandler`: The completion block to be invoked with result when evaluation is complete. Result is YES if the url should be blocked, and NO if it isn’t.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/bebrowsercontentfilter/evaluateurl(_:completionhandler:))*