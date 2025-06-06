# SKRequestDelegate

**Framework**: StoreKit  
**Kind**: protocol

Common methods that are implemented by delegates for any subclass of the `SKRequest` abstract class.

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
protocol SKRequestDelegate : NSObjectProtocol
```

## Topics

### Completing Requests
- [func requestDidFinish(SKRequest)](skrequestdelegate/requestdidfinish(_:).md)
  Tells the delegate that the request has completed.
### Handling Errors
- [func request(SKRequest, didFailWithError: any Error)](skrequestdelegate/request(_:didfailwitherror:).md)
  Tells the delegate that the request failed to execute.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [SKProductsRequestDelegate](skproductsrequestdelegate.md)

## See Also

- [var delegate: (any SKRequestDelegate)?](skrequest/delegate.md)
  The delegate of the request object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skrequestdelegate)*