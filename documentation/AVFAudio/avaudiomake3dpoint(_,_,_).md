# AVAudioMake3DPoint(_:_:_:)

**Framework**: AVFAudio  
**Kind**: func  
**Role**: Function

Creates a 3D point using the x, y, and z coordinates you specify.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func AVAudioMake3DPoint(_ x: Float, _ y: Float, _ z: Float) -> AVAudio3DPoint
```

```c
static AVAudio3DPoint AVAudioMake3DPoint(float x, float y, float z);
```

## Return Value

A new [`AVAudio3DPoint`](./avaudio3dpoint.md) instance.

## Parameters

- `x`: The location on the x-axis, in meters.
- `y`: The location on the y-axis, in meters.
- `z`: The location on the z-axis, in meters.

## See Also

### Creating a point
- [init()](./avaudio3dpoint/init%28%29.md)
  Creates a 3D point.
- [init(x: Float, y: Float, z: Float)](./avaudio3dpoint/init%28x,y,z%29.md)
  Creates a 3D point using the x, y, and z coordinates you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiomake3dpoint(_:_:_:))*