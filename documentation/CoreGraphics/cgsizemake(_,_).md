# CGSizeMake(_:_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns a size with the specified dimension values.

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
func CGSizeMake(_ width: CGFloat, _ height: CGFloat) -> CGSize
```

```c
static CGSize CGSizeMake(CGFloat width, CGFloat height);
```

#### Return Value

Returns a [`CGSize`](../CoreFoundation/cgsize.md) structure with the specified width and height.

## Parameters

- `width`: A width value.
- `height`: A height value.

## See Also

### Creating a Geometric Primitive from Values
- [func CGPointMake(CGFloat, CGFloat) -> CGPoint](./cgpointmake%28_,_%29.md)
  Returns a point with the specified coordinates.
- [func CGRectMake(CGFloat, CGFloat, CGFloat, CGFloat) -> CGRect](./cgrectmake%28_,_,_,_%29.md)
  Returns a rectangle with the specified coordinate and size values.
- [func CGVectorMake(CGFloat, CGFloat) -> CGVector](./cgvectormake%28_,_%29.md)
  Returns a vector with the specified dimension values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgsizemake(_:_:))*