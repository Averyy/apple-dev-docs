# onHingeChange(isEnabled:_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Adds an action to perform when the hinge context of the view hierarchy changes.

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
nonisolated
func onHingeChange(isEnabled: Bool = true, _ action: @escaping (DeviceHingeContext, DeviceHingeContext) -> Void) -> some View
```

## Discussion

Use this modifier to be informed of changes to the hinge context of the device.

SwiftUI calls `action` with the initial hinge context, and again whenever the context changes. When `isEnabled` becomes `false`, if the last context `action` received had a hinge, SwiftUI calls `action` once more with no hinge. After that, SwiftUI doesn’t call `action` until `isEnabled` becomes `true`, and then calls it with the current hinge context if one is available.

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

> ❗ **Important**: Use hinge updates when your app treats the hinge as input, such as driving an animation that responds to granular hinge angle changes, controlling a game, or showing the current angle. Hinge updates arrive while the hinge is moving, at a pace the system sets.
>
> Don’t use hinge updates for layout. To adapt your layout to the fold, use [`ArrangementView`](../arrangementview.md) or [`ReservedRegion`](../reservedregion.md) instead. Reserved region updates arrive during a layout pass, which might be animated.

## See Also

### Responding to hinge angle changes
- [struct DeviceHingeContext](../devicehingecontext.md)
  A type describing the context of hinges on the device.
- [struct DeviceHinge](../devicehinge.md)
  A type encapsulating the state of a single hinge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/onhingechange(isenabled:_:))*