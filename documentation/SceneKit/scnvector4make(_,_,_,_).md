# SCNVector4Make(_:_:_:_:)

**Framework**: SceneKit  
**Kind**: func  
**Role**: Function

Returns a new four-component vector created from individual component values.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```swift
func SCNVector4Make(_ x: Float, _ y: Float, _ z: Float, _ w: Float) -> SCNVector4
```

*macOS*

```swift
func SCNVector4Make(_ x: CGFloat, _ y: CGFloat, _ z: CGFloat, _ w: CGFloat) -> SCNVector4
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```c
static SCNVector4 SCNVector4Make(float x, float y, float z, float w);
```

*macOS*

```c
static SCNVector4 SCNVector4Make(CGFloat x, CGFloat y, CGFloat z, CGFloat w);
```

#### Return Value

An initialized [`SCNVector4`](./scnvector4.md) structure.

## Parameters

- `x`: The first component of the vector.
- `y`: The second component of the vector.
- `z`: The third component of the vector.
- `w`: The fourth component of the vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnvector4make(_:_:_:_:))*