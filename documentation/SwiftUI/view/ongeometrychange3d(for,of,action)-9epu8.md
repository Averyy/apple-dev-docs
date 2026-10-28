# onGeometryChange3D(for:of:action:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Returns a new view that arranges to call `action(oldValue, newValue)` whenever the value computed by `value(proxy)` changes, where `proxy` provides access to the view’s 3D geometry properties.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency func onGeometryChange3D<T>(for type: T.Type, of transform: @escaping (GeometryProxy3D) -> T, action: @escaping (T, T) -> Void) -> some View where T : Equatable
```

**Other overloads**:

```swift
@MainActor
@preconcurrency func onGeometryChange3D<T>(for type: T.Type, of transform: @escaping (GeometryProxy3D) -> T, action: @escaping (T) -> Void) -> some View where T : Equatable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/ongeometrychange3d(for:of:action:)-9epu8)*