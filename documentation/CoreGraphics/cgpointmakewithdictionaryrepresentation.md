# CGPointMakeWithDictionaryRepresentation(_:_:)

**Framework**: Core Graphics  
**Kind**: func

Fills in a point using the contents of the specified dictionary.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGPointMakeWithDictionaryRepresentation(_ dict: CFDictionary, _ point: UnsafeMutablePointer<CGPoint>) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if successful; otherwise [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `dict`: A dictionary that was previously returned from the function  .
- `point`: On return, the point created from the provided dictionary.

## See Also

- [func CGSizeMakeWithDictionaryRepresentation(CFDictionary, UnsafeMutablePointer<CGSize>) -> Bool](cgsizemakewithdictionaryrepresentation(_:_:).md)
  Fills in a size using the contents of the specified dictionary.
- [func CGRectMakeWithDictionaryRepresentation(CFDictionary, UnsafeMutablePointer<CGRect>) -> Bool](cgrectmakewithdictionaryrepresentation(_:_:).md)
  Fills in a rectangle using the contents of the specified dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpointmakewithdictionaryrepresentation(_:_:))*