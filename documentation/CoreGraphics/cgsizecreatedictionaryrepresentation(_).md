# CGSizeCreateDictionaryRepresentation(_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns a dictionary representation of the specified size.

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
func CGSizeCreateDictionaryRepresentation(_ size: CGSize) -> CFDictionary
```

```c
extern CFDictionaryRefCGSizeCreateDictionaryRepresentation(CGSize size);
```

## Return Value

The dictionary representation of the size.

## Parameters

- `size`: A size.

## See Also

### Creating a Dictionary Representation from a Geometric Primitive
- [func CGPointCreateDictionaryRepresentation(CGPoint) -> CFDictionary](./cgpointcreatedictionaryrepresentation%28_%29.md)
  Returns a dictionary representation of the specified point.
- [func CGRectCreateDictionaryRepresentation(CGRect) -> CFDictionary](./cgrectcreatedictionaryrepresentation%28_%29.md)
  Returns a dictionary representation of the provided rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgsizecreatedictionaryrepresentation(_:))*