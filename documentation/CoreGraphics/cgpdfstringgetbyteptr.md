# CGPDFStringGetBytePtr(_:)

**Framework**: Core Graphics  
**Kind**: func

Returns a pointer to the bytes of a PDF string.

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
func CGPDFStringGetBytePtr(_ string: CGPDFStringRef) -> UnsafePointer<UInt8>?
```

#### Return Value

Returns a pointer to the bytes of the specified string. If the string is `NULL`, the function returns `NULL`.

## Parameters

- `string`: A PDF string.

## See Also

- [func CGPDFStringGetLength(CGPDFStringRef) -> Int](cgpdfstringgetlength(_:).md)
  Returns the number of bytes in a PDF string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfstringgetbyteptr(_:))*