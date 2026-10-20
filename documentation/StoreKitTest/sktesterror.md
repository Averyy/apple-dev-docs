# SKTestError

**Framework**: StoreKit Test  
**Kind**: struct  
**Role**: Structure

Information about an error that the testing environment returns.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
struct SKTestError
```

## Topics

### Error Domain
- [static var errorDomain: String](./sktesterror/errordomain.md)
  The domain of the error.
### Error Codes
- [static var fileNotFound: SKTestError.Code](./sktesterror/filenotfound.md)
  The initializer can’t find the file.
- [static var invalidAction: SKTestError.Code](./sktesterror/invalidaction.md)
  The action is invalid.
- [static var invalidProductIdentifier: SKTestError.Code](./sktesterror/invalidproductidentifier.md)
  The product identifier is invalid.
- [static var invalidProductType: SKTestError.Code](./sktesterror/invalidproducttype.md)
  The product type is invalid.
- [static var invalidURL: SKTestError.Code](./sktesterror/invalidurl.md)
  The URL is invalid.
- [static var noSubscriptionFound: SKTestError.Code](./sktesterror/nosubscriptionfound.md)
  The test environment didn’t find a subscription.
- [static var noTransactionFound: SKTestError.Code](./sktesterror/notransactionfound.md)
  The test environment didn’t find a transaction.
- [static var serviceUnavailable: SKTestError.Code](./sktesterror/serviceunavailable.md)
  The service isn’t available.
- [SKTestError.Code](./sktesterror/code.md)
  Error codes in the testing environment.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/customnserror.md)
- [Equatable](../Swift/equatable.md)
- [Error](../Swift/error.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### StoreKit transaction testing errors
- [let SKTestErrorDomain: String](./sktesterrordomain.md)
  A constant that represents the domain for error codes in the testing environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktesterror)*