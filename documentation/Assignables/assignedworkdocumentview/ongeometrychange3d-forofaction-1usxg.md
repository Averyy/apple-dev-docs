# onGeometryChange3D(for:of:action:)

**Framework**: Assignables  
**Kind**: method

Returns a new view that arranges to call `action(value)` whenever the value computed by `transform(proxy)` changes, where `proxy` provides access to the view’s 3D geometry properties.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency func onGeometryChange3D<T>(for type: T.Type, of transform: @escaping (GeometryProxy3D) -> T, action: @escaping (T) -> Void) -> some View where T : Equatable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocumentview/ongeometrychange3d(for:of:action:)-1usxg)*