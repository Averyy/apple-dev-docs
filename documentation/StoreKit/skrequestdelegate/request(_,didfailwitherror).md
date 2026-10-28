# request(_:didFailWithError:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the request failed to execute.

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
optional func request(_ request: SKRequest, didFailWithError error: any Error)
```

```objc
- (void) request:(SKRequest *) request didFailWithError:(NSError *) error;
```

## Mentions

- [Handling errors](../handling-errors.md)

## Discussion

When the request fails, your application should release the request. The [`requestDidFinish(_:)`](./requestdidfinish%28_%29.md) method is not called after this method is called.

## Parameters

- `request`: The request that failed.
- `error`: The error that caused the request to fail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skrequestdelegate/request(_:didfailwitherror:))*