# CGRectCreateDictionaryRepresentation(_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns a dictionary representation of the provided rectangle.

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
func CGRectCreateDictionaryRepresentation(_: CGRect) -> CFDictionary
```

```c
extern CFDictionaryRefCGRectCreateDictionaryRepresentation(CGRect );
```

## Return Value

The dictionary representation of the rectangle.

## See Also

### Creating a Dictionary Representation from a Geometric Primitive
- [func CGPointCreateDictionaryRepresentation(CGPoint) -> CFDictionary](./cgpointcreatedictionaryrepresentation%28_%29.md)
  Returns a dictionary representation of the specified point.
- [func CGSizeCreateDictionaryRepresentation(CGSize) -> CFDictionary](./cgsizecreatedictionaryrepresentation%28_%29.md)
  Returns a dictionary representation of the specified size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgrectcreatedictionaryrepresentation(_:))*