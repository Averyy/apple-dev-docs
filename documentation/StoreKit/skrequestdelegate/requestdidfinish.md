# requestDidFinish(_:)

**Framework**: StoreKit  
**Kind**: method

Tells the delegate that the request has completed.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
optional func requestDidFinish(_ request: SKRequest)
```

#### Discussion

This method is called after all processing of the request has been completed. Typically, subclasses of [`SKRequest`](skrequest.md) require the delegate to implement additional methods to receive the response. When this method is called, your delegate receives no further communication from the request and can release it.

## Parameters

- `request`: The request that completed.

## See Also

- [In-App Purchase Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skrequestdelegate/requestdidfinish(_:))*