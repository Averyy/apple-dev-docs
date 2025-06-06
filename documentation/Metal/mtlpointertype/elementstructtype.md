# elementStructType()

**Framework**: Metal  
**Kind**: method

Provides a description of the underlying struct when the pointer points to a struct.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func elementStructType() -> MTLStructType?
```

#### Return Value

An object that describes the struct. If the pointer does not point to an struct, this method returns `nil`.

## See Also

- [func elementArrayType() -> MTLArrayType?](mtlpointertype/elementarraytype.md)
  Provides a description of the underlying array when the pointer points to an array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpointertype/elementstructtype())*