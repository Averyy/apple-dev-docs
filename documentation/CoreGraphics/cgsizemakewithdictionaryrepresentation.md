# CGSizeMakeWithDictionaryRepresentation(_:_:)

**Framework**: Core Graphics  
**Kind**: func

Fills in a size using the contents of the specified dictionary.

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
func CGSizeMakeWithDictionaryRepresentation(_ dict: CFDictionary, _ size: UnsafeMutablePointer<CGSize>) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if successful; otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `dict`: A dictionary that was previously returned from the function  .
- `size`: On return, the size created from the specified dictionary.

## See Also

- [func CGPointMakeWithDictionaryRepresentation(CFDictionary, UnsafeMutablePointer<CGPoint>) -> Bool](cgpointmakewithdictionaryrepresentation(_:_:).md)
  Fills in a point using the contents of the specified dictionary.
- [func CGRectMakeWithDictionaryRepresentation(CFDictionary, UnsafeMutablePointer<CGRect>) -> Bool](cgrectmakewithdictionaryrepresentation(_:_:).md)
  Fills in a rectangle using the contents of the specified dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgsizemakewithdictionaryrepresentation(_:_:))*