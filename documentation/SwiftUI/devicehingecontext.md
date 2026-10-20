# DeviceHingeContext

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A type describing the context of hinges on the device.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
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
- [var hinge: DeviceHinge?](./devicehingecontext/hinge.md)
  The current hinge of the device.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Responding to hinge angle changes
- [func onHingeChange(isEnabled: Bool, (DeviceHingeContext, DeviceHingeContext) -> Void) -> some View](./view/onhingechange%28isenabled,_%29.md)
  Adds an action to perform when the hinge context of the view hierarchy changes.
- [struct DeviceHinge](./devicehinge.md)
  A type encapsulating the state of a single hinge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/devicehingecontext)*