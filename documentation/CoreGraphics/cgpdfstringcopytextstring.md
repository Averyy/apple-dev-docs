# CGPDFStringCopyTextString(_:)

**Framework**: Core Graphics  
**Kind**: func

Returns a CFString object that represents a PDF string as a text string.

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
func CGPDFStringCopyTextString(_ string: CGPDFStringRef) -> CFString?
```

#### Return Value

Returns a CFString object that represents the specified PDF string as a text string. You are responsible for releasing this object.

## Parameters

- `string`: A PDF string. If this value is  , it will cause an error.

## See Also

- [func CGPDFStringCopyDate(CGPDFStringRef) -> CFDate?](cgpdfstringcopydate(_:).md)
  Converts a string to a date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfstringcopytextstring(_:))*