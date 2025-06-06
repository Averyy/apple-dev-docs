# request(_:didFailWithError:)

**Framework**: StoreKit  
**Kind**: method

Tells the delegate that the request failed to execute.

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
optional func request(_ request: SKRequest, didFailWithError error: any Error)
```

## Mentions

- [Handling errors](handling-errors.md)

#### Discussion

When the request fails, your application should release the request. The [`requestDidFinish(_:)`](skrequestdelegate/requestdidfinish(_:).md) method is not called after this method is called.

## Parameters

- `request`: The request that failed.
- `error`: The error that caused the request to fail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skrequestdelegate/request(_:didfailwitherror:))*