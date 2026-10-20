# objectAlreadyAssociatedToHome

**Framework**: HomeKit  
**Kind**: property  
**Role**: Type Property

An attempt to associate an object with a home when it’s already associated with that home.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var objectAlreadyAssociatedToHome: HMError.Code { get }
```

## See Also

### Detecting association errors
- [static var invalidAssociatedServiceType: HMError.Code](./invalidassociatedservicetype.md)
  An error indicating an invalid service type.
- [static var objectAssociatedToAnotherHome: HMError.Code](./objectassociatedtoanotherhome.md)
  An attempt to associate an object with a home when it’s already associated with another home.
- [static var objectNotAssociatedToAnyHome: HMError.Code](./objectnotassociatedtoanyhome.md)
  An attempt to perform an operation on an object that is not associated to any home.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmerror/objectalreadyassociatedtohome)*