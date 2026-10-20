# services

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

An array of services that represents this profile.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var services: [HMService] { get }
```

```objc
@property (nonatomic, strong, readonly) NSArray<HMService *> * services;
```

## See Also

### Getting information about a profile
- [var accessory: HMAccessory?](./accessory.md)
  The accessory that implements this profile.
- [var uniqueIdentifier: UUID](./uniqueidentifier.md)
  A unique identifier for the profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessoryprofile/services)*