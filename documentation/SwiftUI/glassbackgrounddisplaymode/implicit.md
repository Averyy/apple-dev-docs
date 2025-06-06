# GlassBackgroundDisplayMode.implicit

**Framework**: SwiftUI  
**Kind**: case

Display the glass material only when the view isn’t already contained in glass.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
case implicit
```

#### Discussion

Use this value to avoid duplicate backgrounds when a view that has a glass background contains another view that also has a glass background.

This display mode doesn’t suppress duplicate glass backgrounds for views that are offset by any amount in the z-axis. For example, the two subviews of the following [`HStack`](hstack.md) behave differently:

```swift
HStack {
    MyView()
        .glassBackgroundEffect(displayMode: .implicit)
    MyView()
        .glassBackgroundEffect(displayMode: .implicit)
        .offset(z: 100)
}
.glassBackgroundEffect(displayMode: .always)
```

The first instance of `MyView` doesn’t display a background because its container displays one. However the second instance does display a background because that view is offset from its container by 100 points along the z-axis.

## See Also

- [GlassBackgroundDisplayMode.always](glassbackgrounddisplaymode/always.md)
  Always display the glass material.
- [GlassBackgroundDisplayMode.never](glassbackgrounddisplaymode/never.md)
  Never display the glass material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/glassbackgrounddisplaymode/implicit)*