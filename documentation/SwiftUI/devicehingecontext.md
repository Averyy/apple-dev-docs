# DeviceHingeContext

**Framework**: SwiftUI  
**Kind**: struct

A type describing the context of hinges on the device.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)
- Mac Catalyst 27.1+
- macOS 27.1+
- tvOS 27.1+
- visionOS 27.1+
- watchOS 27.1+

## Declaration

```swift
struct DeviceHingeContext
```

#### Overview

You use this type with the `View/onHingeChange(_:)` view modifier.

## Topics

### Getting hinge context information
- [var hinge: DeviceHinge?](devicehingecontext/hinge.md)
  The current hinge of the device.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func onHingeChange(isEnabled: Bool, (DeviceHingeContext, DeviceHingeContext) -> Void) -> some View](view/onhingechange(isenabled:_:).md)
  Adds an action to perform when the hinge context of the view hierarchy changes.
- [struct DeviceHinge](devicehinge.md)
  A type encapsulating the state of a single hinge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/devicehingecontext)*