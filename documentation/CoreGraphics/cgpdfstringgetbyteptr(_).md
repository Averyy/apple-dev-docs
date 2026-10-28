# CGPDFStringGetBytePtr(_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns a pointer to the bytes of a PDF string.

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
func CGPDFStringGetBytePtr(_ string: CGPDFStringRef) -> UnsafePointer<UInt8>?
```

```c
extern const unsigned char *CGPDFStringGetBytePtr(CGPDFStringRef string);
```

## Return Value

Returns a pointer to the bytes of the specified string. If the string is `NULL`, the function returns `NULL`.

## Parameters

- `string`: A PDF string.

## See Also

### Getting PDF String Data
- [func CGPDFStringGetLength(CGPDFStringRef) -> Int](./cgpdfstringgetlength%28_%29.md)
  Returns the number of bytes in a PDF string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfstringgetbyteptr(_:))*