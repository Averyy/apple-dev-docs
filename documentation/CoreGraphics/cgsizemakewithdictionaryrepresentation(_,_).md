# CGSizeMakeWithDictionaryRepresentation(_:_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Fills in a size using the contents of the specified dictionary.

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
func CGSizeMakeWithDictionaryRepresentation(_ dict: CFDictionary, _ size: UnsafeMutablePointer<CGSize>) -> Bool
```

```c
extern bool CGSizeMakeWithDictionaryRepresentation(CFDictionaryRef dict, CGSize *size);
```

#### Return Value

[`true`](../Swift/true.md) if successful; otherwise [`false`](../Swift/false.md).

## Parameters

- `dict`: A dictionary that was previously returned from the function [`CGSizeCreateDictionaryRepresentation(_:)`](./cgsizecreatedictionaryrepresentation%28_%29.md).
- `size`: On return, the size created from the specified dictionary.

## See Also

### Creating a Geometric Primitive from a Dictionary Representation
- [func CGPointMakeWithDictionaryRepresentation(CFDictionary, UnsafeMutablePointer<CGPoint>) -> Bool](./cgpointmakewithdictionaryrepresentation%28_,_%29.md)
  Fills in a point using the contents of the specified dictionary.
- [func CGRectMakeWithDictionaryRepresentation(CFDictionary, UnsafeMutablePointer<CGRect>) -> Bool](./cgrectmakewithdictionaryrepresentation%28_,_%29.md)
  Fills in a rectangle using the contents of the specified dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgsizemakewithdictionaryrepresentation(_:_:))*