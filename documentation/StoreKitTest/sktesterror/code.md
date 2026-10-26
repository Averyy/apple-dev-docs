# SKTestError.Code

**Framework**: StoreKit Test  
**Kind**: enum  
**Role**: Enumeration

Error codes in the testing environment.

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
enum Code
```

```c
enum SKTestErrorCode : NSInteger;
```

## Topics

### Error Codes
- [SKTestError.Code.fileNotFound](./code/filenotfound.md)
  The initializer can’t find the file.
- [SKTestError.Code.invalidAction](./code/invalidaction.md)
  The action is invalid.
- [SKTestError.Code.invalidProductIdentifier](./code/invalidproductidentifier.md)
  The product identifier is invalid.
- [SKTestError.Code.invalidProductType](./code/invalidproducttype.md)
  The product type is invalid.
- [SKTestError.Code.invalidURL](./code/invalidurl.md)
  The URL is invalid.
- [SKTestError.Code.noSubscriptionFound](./code/nosubscriptionfound.md)
  The test environment didn’t find a subscription.
- [SKTestError.Code.noTransactionFound](./code/notransactionfound.md)
  The test environment didn’t find a transaction.
- [SKTestError.Code.serviceUnavailable](./code/serviceunavailable.md)
  The service isn’t available.
- [SKTestError.Code.fileNotFound](./code/filenotfound.md)
  The initializer can’t find the file.
- [SKTestError.Code.invalidAction](./code/invalidaction.md)
  The action is invalid.
- [SKTestError.Code.invalidProductIdentifier](./code/invalidproductidentifier.md)
  The product identifier is invalid.
- [SKTestError.Code.invalidProductType](./code/invalidproducttype.md)
  The product type is invalid.
- [SKTestError.Code.invalidURL](./code/invalidurl.md)
  The URL is invalid.
- [SKTestError.Code.noSubscriptionFound](./code/nosubscriptionfound.md)
  The test environment didn’t find a subscription.
- [SKTestError.Code.noTransactionFound](./code/notransactionfound.md)
  The test environment didn’t find a transaction.
- [SKTestError.Code.serviceUnavailable](./code/serviceunavailable.md)
  The service isn’t available.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### StoreKit transaction testing errors
- [SKTestErrorDomain](../sktesterrordomain.md)
  A constant that represents the domain for error codes in the testing environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktesterror/code)*