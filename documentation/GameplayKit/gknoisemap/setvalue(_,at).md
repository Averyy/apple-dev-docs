# setValue(_:at:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

Sets the value at the specified position in the noise map.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func setValue(_ value: Float, at position: vector_int2)
```

```objc
- (void) setValue:(float) value atPosition:(vector_int2) position;
```

#### Discussion

## Parameters

- `value`: The new value to set.
- `position`: A position in the noise map’s integer grid.

## See Also

### Accessing Noise Values
- [func value(at: vector_int2) -> Float](./value%28at%29.md)
  Returns the value at the specified position in the noise map’s discrete sample grid.
- [func interpolatedValue(at: vector_float2) -> Float](./interpolatedvalue%28at%29.md)
  Returns the value at the specified position in the noise map, interpolating results for positions not on the discrete sample grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknoisemap/setvalue(_:at:))*