# elementArrayType()

**Framework**: Metal  
**Kind**: method

Provides a description of the underlying array when the pointer points to an array.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func elementArrayType() -> MTLArrayType?
```

#### Return Value

An object that describes the array. If the pointer does not point to an array, this method returns `nil`.

## See Also

- [func elementStructType() -> MTLStructType?](mtlpointertype/elementstructtype.md)
  Provides a description of the underlying struct when the pointer points to a struct.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpointertype/elementarraytype())*