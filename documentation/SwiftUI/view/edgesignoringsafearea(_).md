# edgesIgnoringSafeArea(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Changes the view’s proposed area to extend outside the screen’s safe areas.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- macOS 10.15+ - Deprecated in 27.2
- tvOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 6.0+ - Deprecated in 27.2

> **Deprecated**: Use [`ignoresSafeArea(_:edges:)`](./ignoressafearea%28_,edges%29.md) instead.

## Declaration

```swift
nonisolated
func edgesIgnoringSafeArea(_ edges: Edge.Set) -> some View
```

#### Return Value

A view that may extend outside of the screen’s safe area on the edges specified by `edges`.

#### Discussion

Use `edgesIgnoringSafeArea(_:)` to change the area proposed for this view so that — were the proposal accepted — this view could extend outside the safe area to the bounds of the screen for the specified edges.

For example, you can propose that a text view ignore the safe area’s top inset:

```swift
VStack {
    Text("This text is outside of the top safe area.")
        .edgesIgnoringSafeArea([.top])
        .border(Color.purple)
    Text("This text is inside VStack.")
        .border(Color.yellow)
}
.border(Color.gray)
```

![A screenshot showing a view whose bounds exceed the safe area of the screen.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-View-edgesIgnoringSafeArea@2x.png)

Depending on the surrounding view hierarchy, SwiftUI may not honor an `edgesIgnoringSafeArea(_:)` request. This can happen, for example, if the view is inside a container that respects the screen’s safe area. In that case you may need to apply `edgesIgnoringSafeArea(_:)` to the container instead.

## Parameters

- `edges`: The set of the edges in which to expand the size requested for this view.

## See Also

### Layout modifiers
- [func frame() -> some View](./frame%28%29.md)
  Positions this view within an invisible frame.
- [func coordinateSpace<T>(name: T) -> some View](./coordinatespace%28name%29.md)
  Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/edgesignoringsafearea(_:))*