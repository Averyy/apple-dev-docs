# CGRectMakeWithDictionaryRepresentation(_:_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Fills in a rectangle using the contents of the specified dictionary.

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
func CGRectMakeWithDictionaryRepresentation(_ dict: CFDictionary, _ rect: UnsafeMutablePointer<CGRect>) -> Bool
```

```c
extern bool CGRectMakeWithDictionaryRepresentation(CFDictionaryRef dict, CGRect *rect);
```

#### Return Value

[`true`](../Swift/true.md) if successful; otherwise [`false`](../Swift/false.md).

## Parameters

- `dict`: A dictionary that was previously returned from the function [`CGRectCreateDictionaryRepresentation(_:)`](./cgrectcreatedictionaryrepresentation%28_%29.md).
- `rect`: On return, the rectangle created from the specified dictionary.

## See Also

### Creating a Geometric Primitive from a Dictionary Representation
- [func CGPointMakeWithDictionaryRepresentation(CFDictionary, UnsafeMutablePointer<CGPoint>) -> Bool](./cgpointmakewithdictionaryrepresentation%28_,_%29.md)
  Fills in a point using the contents of the specified dictionary.
- [func CGSizeMakeWithDictionaryRepresentation(CFDictionary, UnsafeMutablePointer<CGSize>) -> Bool](./cgsizemakewithdictionaryrepresentation%28_,_%29.md)
  Fills in a size using the contents of the specified dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgrectmakewithdictionaryrepresentation(_:_:))*