# CGPointCreateDictionaryRepresentation(_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns a dictionary representation of the specified point.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGPointCreateDictionaryRepresentation(_ point: CGPoint) -> CFDictionary
```

```c
extern CFDictionaryRefCGPointCreateDictionaryRepresentation(CGPoint point);
```

#### Return Value

The dictionary representation of the point.

## Parameters

- `point`: A point.

## See Also

### Creating a Dictionary Representation from a Geometric Primitive
- [func CGSizeCreateDictionaryRepresentation(CGSize) -> CFDictionary](./cgsizecreatedictionaryrepresentation%28_%29.md)
  Returns a dictionary representation of the specified size.
- [func CGRectCreateDictionaryRepresentation(CGRect) -> CFDictionary](./cgrectcreatedictionaryrepresentation%28_%29.md)
  Returns a dictionary representation of the provided rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpointcreatedictionaryrepresentation(_:))*