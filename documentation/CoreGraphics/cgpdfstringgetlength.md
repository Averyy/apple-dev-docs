# CGPDFStringGetLength(_:)

**Framework**: Core Graphics  
**Kind**: func

Returns the number of bytes in a PDF string.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGPDFStringGetLength(_ string: CGPDFStringRef) -> Int
```

#### Return Value

Returns the number of bytes referenced by the string, or `0` if the string is `NULL`.

## Parameters

- `string`: A PDF string.

## See Also

- [func CGPDFStringGetBytePtr(CGPDFStringRef) -> UnsafePointer<UInt8>?](cgpdfstringgetbyteptr(_:).md)
  Returns a pointer to the bytes of a PDF string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfstringgetlength(_:))*