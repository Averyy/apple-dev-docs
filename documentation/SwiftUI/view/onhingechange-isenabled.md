# onHingeChange(isEnabled:_:)

**Framework**: SwiftUI  
**Kind**: method

Adds an action to perform when the hinge context of the view hierarchy changes.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
nonisolated
func onHingeChange(isEnabled: Bool = true, _ action: @escaping (DeviceHingeContext, DeviceHingeContext) -> Void) -> some View
```

#### Discussion

Use this modifier to be informed of changes to the hinge context of the device.

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

## See Also

- [struct DeviceHingeContext](devicehingecontext.md)
  A type describing the context of hinges on the device.
- [struct DeviceHinge](devicehinge.md)
  A type encapsulating the state of a single hinge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/onhingechange(isenabled:_:))*