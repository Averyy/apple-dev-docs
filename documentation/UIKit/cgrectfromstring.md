# CGRectFromString

**Framework**: UIKit  
**Kind**: func  
**Role**: Function

Returns a Core Graphics rectangle structure corresponding to the data in a given string.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS 2.0+

## Declaration

```c
extern CGRect CGRectFromString(NSString *string);
```

#### Return Value

A Core Graphics structure that represents a rectangle. If the string is not well-formed, the function returns [`CGRectZero`](../CoreGraphics/cgrectzero.md).

#### Discussion

In general, you should use this function only to convert strings that were previously created using the [`NSStringFromCGRect`](./nsstringfromcgrect.md) function.

## Parameters

- `string`: A string whose contents are of the form “{{*x*,*y*},{*w*, *h*}}”, where *x* is the x coordinate, *y* is the y coordinate, *w* is the width, and *h* is the height. These components can represent integer or float values. An example of a valid string is `@"{{3,2},{4,5}}"`. The string is not localized, so items are always separated with a comma.

## See Also

### Primitive type conversions
- [CGAffineTransformFromString](./cgaffinetransformfromstring.md)
  Returns a Core Graphics affine transform structure corresponding to the data in a given string.
- [CGPointFromString](./cgpointfromstring.md)
  Returns a Core Graphics point structure corresponding to the data in a given string.
- [CGSizeFromString](./cgsizefromstring.md)
  Returns a Core Graphics size structure corresponding to the data in a given string.
- [CGVectorFromString](./cgvectorfromstring.md)
  Returns a Core Graphics vector corresponding to the data in a given string.
- [NSStringFromCGAffineTransform](./nsstringfromcgaffinetransform.md)
  Returns a string formatted to contain the data from an affine transform.
- [NSStringFromCGPoint](./nsstringfromcgpoint.md)
  Returns a string formatted to contain the data from a point.
- [NSStringFromCGRect](./nsstringfromcgrect.md)
  Returns a string formatted to contain the data from a rectangle.
- [NSStringFromCGSize](./nsstringfromcgsize.md)
  Returns a string formatted to contain the data from a size data structure.
- [NSStringFromCGVector](./nsstringfromcgvector.md)
  Returns a string formatted to contain the data from a vector data structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/cgrectfromstring)*