# identifier

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The identifier for the PPK.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var identifier: String { get }
```

```objc
@property (copy, readonly) NSString * identifier;
```

## See Also

### Accessing the configuration parameters
- [var keychainReference: Data](./keychainreference.md)
  A persistent reference to the key in the keychain.
- [var isMandatory: Bool](./ismandatory.md)
  A Boolean value that indicates whether it’s mandatory for the VPN server to use this PPK.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnikev2ppkconfiguration/identifier)*