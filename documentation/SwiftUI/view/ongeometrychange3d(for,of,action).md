# onGeometryChange3D(for:of:action:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Returns a new view that arranges to call `action(value)` whenever the value computed by `transform(proxy)` changes, where `proxy` provides access to the view’s 3D geometry properties.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency func onGeometryChange3D<T>(for type: T.Type, of transform: @escaping (GeometryProxy3D) -> T, action: @escaping (T) -> Void) -> some View where T : Equatable
```

**Other overloads**:

```swift
@MainActor
@preconcurrency func onGeometryChange3D<T>(for type: T.Type, of transform: @escaping (GeometryProxy3D) -> T, action: @escaping (T, T) -> Void) -> some View where T : Equatable
```

## See Also

### Geometry
- [func onGeometryChange(for:of:action:)](./ongeometrychange%28for,of,action%29.md)
  Adds an action to be performed when a value, created from a geometry proxy, changes.
- [func onInteractiveResizeChange((Bool) -> Void) -> some View](./oninteractiveresizechange%28_%29.md)
  Adds an action to perform when the enclosing window is being interactively resized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/ongeometrychange3d(for:of:action:))*