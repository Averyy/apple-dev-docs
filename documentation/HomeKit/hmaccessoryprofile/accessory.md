# accessory

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The accessory that implements this profile.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
weak var accessory: HMAccessory? { get }
```

```objc
@property (nonatomic, weak, readonly) HMAccessory * accessory;
```

## See Also

### Getting information about a profile
- [var services: [HMService]](./services.md)
  An array of services that represents this profile.
- [var uniqueIdentifier: UUID](./uniqueidentifier.md)
  A unique identifier for the profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessoryprofile/accessory)*