# SCNVector3Make(_:_:_:)

**Framework**: SceneKit  
**Kind**: func  
**Role**: Function

Returns a new three-component vector created from individual component values.

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
func SCNVector3Make(_ x: Float, _ y: Float, _ z: Float) -> SCNVector3
```

*macOS*

```swift
func SCNVector3Make(_ x: CGFloat, _ y: CGFloat, _ z: CGFloat) -> SCNVector3
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```c
static SCNVector3 SCNVector3Make(float x, float y, float z);
```

*macOS*

```c
static SCNVector3 SCNVector3Make(CGFloat x, CGFloat y, CGFloat z);
```

#### Return Value

An initialized [`SCNVector3`](./scnvector3.md) structure.

## Parameters

- `x`: The first component of the vector.
- `y`: The second component of the vector.
- `z`: The third component of the vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnvector3make(_:_:_:))*