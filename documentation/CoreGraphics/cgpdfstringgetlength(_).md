# CGPDFStringGetLength(_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns the number of bytes in a PDF string.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGPDFStringGetLength(_ string: CGPDFStringRef) -> Int
```

```c
extern size_t CGPDFStringGetLength(CGPDFStringRef string);
```

## Return Value

Returns the number of bytes referenced by the string, or `0` if the string is `NULL`.

## Parameters

- `string`: A PDF string.

## See Also

### Getting PDF String Data
- [func CGPDFStringGetBytePtr(CGPDFStringRef) -> UnsafePointer<UInt8>?](./cgpdfstringgetbyteptr%28_%29.md)
  Returns a pointer to the bytes of a PDF string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfstringgetlength(_:))*