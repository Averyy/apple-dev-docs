# CGPointMakeWithDictionaryRepresentation(_:_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Fills in a point using the contents of the specified dictionary.

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
func CGPointMakeWithDictionaryRepresentation(_ dict: CFDictionary, _ point: UnsafeMutablePointer<CGPoint>) -> Bool
```

```c
extern bool CGPointMakeWithDictionaryRepresentation(CFDictionaryRef dict, CGPoint *point);
```

#### Return Value

[`true`](../Swift/true.md) if successful; otherwise [`false`](../Swift/false.md).

## Parameters

- `dict`: A dictionary that was previously returned from the function [`CGPointCreateDictionaryRepresentation(_:)`](./cgpointcreatedictionaryrepresentation%28_%29.md).
- `point`: On return, the point created from the provided dictionary.

## See Also

### Creating a Geometric Primitive from a Dictionary Representation
- [func CGSizeMakeWithDictionaryRepresentation(CFDictionary, UnsafeMutablePointer<CGSize>) -> Bool](./cgsizemakewithdictionaryrepresentation%28_,_%29.md)
  Fills in a size using the contents of the specified dictionary.
- [func CGRectMakeWithDictionaryRepresentation(CFDictionary, UnsafeMutablePointer<CGRect>) -> Bool](./cgrectmakewithdictionaryrepresentation%28_,_%29.md)
  Fills in a rectangle using the contents of the specified dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpointmakewithdictionaryrepresentation(_:_:))*