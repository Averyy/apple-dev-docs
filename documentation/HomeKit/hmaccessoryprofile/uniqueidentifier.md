# uniqueIdentifier

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

A unique identifier for the profile.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var uniqueIdentifier: UUID { get }
```

```objc
@property (nonatomic, copy, readonly) NSUUID * uniqueIdentifier;
```

## See Also

### Getting information about a profile
- [var accessory: HMAccessory?](./accessory.md)
  The accessory that implements this profile.
- [var services: [HMService]](./services.md)
  An array of services that represents this profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessoryprofile/uniqueidentifier)*