# MTLOriginMake(_:_:_:)

**Framework**: Metal  
**Kind**: func  
**Role**: Function

Returns a new origin with the specified coordinates.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
func MTLOriginMake(_ x: Int, _ y: Int, _ z: Int) -> MTLOrigin
```

```c
static MTLOrigin MTLOriginMake(NSUInteger x, NSUInteger y, NSUInteger z);
```

## Return Value

The specified origin point.

## Parameters

- `x`: The x coordinate.
- `y`: The y coordinate.
- `z`: The z coordinate.

## See Also

### Creating origin points
- [init()](./mtlorigin/init%28%29.md)
  Initializes a new origin.
- [init(x: Int, y: Int, z: Int)](./mtlorigin/init%28x,y,z%29.md)
  Initializes a new origin with the specified coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtloriginmake(_:_:_:))*