# requestDidFinish(_:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the request has completed.

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
optional func requestDidFinish(_ request: SKRequest)
```

```objc
- (void) requestDidFinish:(SKRequest *) request;
```

## Discussion

This method is called after all processing of the request has been completed. Typically, subclasses of [`SKRequest`](../skrequest.md) require the delegate to implement additional methods to receive the response. When this method is called, your delegate receives no further communication from the request and can release it.

## Parameters

- `request`: The request that completed.

## See Also

### Related Documentation
- [Apple In-App Purchase Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skrequestdelegate/requestdidfinish(_:))*