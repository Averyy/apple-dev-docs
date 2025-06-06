# invalidAssociatedServiceType

**Framework**: HomeKit  
**Kind**: property

An error indicating an invalid service type.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var invalidAssociatedServiceType: HMError.Code { get }
```

## See Also

- [static var objectAlreadyAssociatedToHome: HMError.Code](hmerror/objectalreadyassociatedtohome.md)
  An attempt to associate an object with a home when it’s already associated with that home.
- [static var objectAssociatedToAnotherHome: HMError.Code](hmerror/objectassociatedtoanotherhome.md)
  An attempt to associate an object with a home when it’s already associated with another home.
- [static var objectNotAssociatedToAnyHome: HMError.Code](hmerror/objectnotassociatedtoanyhome.md)
  An attempt to perform an operation on an object that is not associated to any home.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmerror/invalidassociatedservicetype)*