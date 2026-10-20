# SKRequestDelegate

**Framework**: StoreKit  
**Kind**: protocol  
**Role**: Protocol

Common methods that are implemented by delegates for any subclass of the `SKRequest` abstract class.

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
protocol SKRequestDelegate : NSObjectProtocol
```

```objc
@protocol SKRequestDelegate <NSObject>
```

## Topics

### Completing Requests
- [func requestDidFinish(SKRequest)](./skrequestdelegate/requestdidfinish%28_%29.md)
  Tells the delegate that the request has completed.
### Handling Errors
- [func request(SKRequest, didFailWithError: any Error)](./skrequestdelegate/request%28_,didfailwitherror%29.md)
  Tells the delegate that the request failed to execute.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [SKProductsRequestDelegate](./skproductsrequestdelegate.md)

## See Also

### Accessing the Delegate
- [var delegate: (any SKRequestDelegate)?](./skrequest/delegate.md)
  The delegate of the request object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skrequestdelegate)*