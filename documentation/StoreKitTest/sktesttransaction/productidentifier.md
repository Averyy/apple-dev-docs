# productIdentifier

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Instance Property

An identifier that uniquely represents a product, which you provide in the StoreKit configuration file.

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
var productIdentifier: String { get }
```

```objc
@property (nonatomic, readonly) NSString * productIdentifier;
```

#### Discussion

You configure the product identifiers in the .`storekit` configuration file. Each product identifier must be unique.

> **Note**:  The StoreKitTest framework never accesses App Store Connect, so it doesn’t retrieve actual product identifiers you may have configured there.

## See Also

### Identifying Transactions and Products
- [var identifier: Int](./identifier.md)
  The identifier of the transaction in the testing environment.
- [var originalTransactionIdentifier: Int](./originaltransactionidentifier.md)
  The identifier of the original transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktesttransaction/productidentifier)*