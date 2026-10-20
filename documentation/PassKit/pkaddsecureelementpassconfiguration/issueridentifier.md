# issuerIdentifier

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

An opaque value for the configuration.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS
- visionOS 1.0+

## Declaration

```swift
var issuerIdentifier: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * issuerIdentifier;
```

#### Discussion

> ❗ **Important**:  This property’s value is unique for each issuer. This property is available only to developers who work with Apple to enable this functionality.

## See Also

### Managing the issuer identity
- [var localizedDescription: String?](./localizeddescription.md)
  The configuration’s localized description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddsecureelementpassconfiguration/issueridentifier)*