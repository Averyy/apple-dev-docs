# DeviceHinge

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A type encapsulating the state of a single hinge.

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
struct DeviceHinge
```

#### Overview

A hinge provides its angle along with a status determined by the system based on the current angle and device orientation. You use this type with the `View/onHingeChange(_:)` modifier.

```swift
@State private var hinge: DeviceHinge? = nil

var body: some View {
    VStack {
        if let hinge {
            AngleDisplayView(angle: hinge.angle)
            StatusDisplayView(status: hinge.status)
        } else {
            ContentUnavailableView(
                "Hinge Unavailable",
                systemImage: "rectangle.split.2x1")
        }
    }
    .onHingeChange { _, newContext in
        hinge = newContext.hinge
    }
}
```

In the example above, the current angle and status of the hinge will be displayed in the app as you interact with the hinge.

## Topics

### Getting hinge information
- [var angle: Angle](./devicehinge/angle.md)
  Current angle of the hinge.
- [var status: DeviceHinge.Status](./devicehinge/status-swift.property.md)
  Current status of the hinge.
- [DeviceHinge.Status](./devicehinge/status-swift.struct.md)
  The status of an individual hinge.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Responding to hinge angle changes
- [func onHingeChange(isEnabled: Bool, (DeviceHingeContext, DeviceHingeContext) -> Void) -> some View](./view/onhingechange%28isenabled,_%29.md)
  Adds an action to perform when the hinge context of the view hierarchy changes.
- [struct DeviceHingeContext](./devicehingecontext.md)
  A type describing the context of hinges on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/devicehinge)*