# primaryAccountNumberSuffix

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

A display-ready version of the primary account number.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
var primaryAccountNumberSuffix: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * primaryAccountNumberSuffix;
```

#### Discussion

This property’s value is generally the last four or five digits of the primary account number, but can vary by issuer. The value isn’t related to [`primaryAccountIdentifier`](./primaryaccountidentifier.md).

## See Also

### Getting the account attributes
- [var primaryAccountIdentifier: String](./primaryaccountidentifier.md)
  An opaque value that identifies the primary account number that funds the pass’s transactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pksecureelementpass/primaryaccountnumbersuffix)*