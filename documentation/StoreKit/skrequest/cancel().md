# cancel()

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

Cancels a previously started request.

**Availability**:
- iOS 3.0+ - Deprecated in 18.0
- iPadOS 3.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.7+ - Deprecated in 15.0
- tvOS - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: No longer supported.

## Declaration

```swift
func cancel()
```

```objc
- (void) cancel;
```

## Discussion

When you cancel a request, the delegate is not called with an error.

## See Also

### Controlling the Request
- [func start()](./start%28%29.md)
  Sends the request to the Apple App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skrequest/cancel())*