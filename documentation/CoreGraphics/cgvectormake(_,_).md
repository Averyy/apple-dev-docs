# CGVectorMake(_:_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns a vector with the specified dimension values.

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
func CGVectorMake(_ dx: CGFloat, _ dy: CGFloat) -> CGVector
```

```c
static CGVector CGVectorMake(CGFloat dx, CGFloat dy);
```

#### Return Value

Returns a [`CGVector`](../CoreFoundation/cgvector.md) structure with the specified coordinates.

## Parameters

- `dx`: The x-coordinate of the vector to construct.
- `dy`: The y-coordinate of the vector to construct.

## See Also

### Creating a Geometric Primitive from Values
- [func CGPointMake(CGFloat, CGFloat) -> CGPoint](./cgpointmake%28_,_%29.md)
  Returns a point with the specified coordinates.
- [func CGRectMake(CGFloat, CGFloat, CGFloat, CGFloat) -> CGRect](./cgrectmake%28_,_,_,_%29.md)
  Returns a rectangle with the specified coordinate and size values.
- [func CGSizeMake(CGFloat, CGFloat) -> CGSize](./cgsizemake%28_,_%29.md)
  Returns a size with the specified dimension values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgvectormake(_:_:))*