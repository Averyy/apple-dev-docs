# primaryAccountIdentifier

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

An opaque value that identifies the primary account number that funds the pass’s transactions.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
var primaryAccountIdentifier: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * primaryAccountIdentifier;
```

## See Also

### Getting the account attributes
- [var primaryAccountNumberSuffix: String](./primaryaccountnumbersuffix.md)
  A display-ready version of the primary account number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pksecureelementpass/primaryaccountidentifier)*