# isMandatory

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether it’s mandatory for the VPN server to use this PPK.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var isMandatory: Bool { get set }
```

```objc
@property BOOL isMandatory;
```

#### Discussion

The default value is `true`.

## See Also

### Accessing the configuration parameters
- [var identifier: String](./identifier.md)
  The identifier for the PPK.
- [var keychainReference: Data](./keychainreference.md)
  A persistent reference to the key in the keychain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnikev2ppkconfiguration/ismandatory)*