# CGPDFStringCopyDate(_:)

**Framework**: Core Graphics  
**Kind**: func

Converts a string to a date.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGPDFStringCopyDate(_ string: CGPDFStringRef) -> CFDate?
```

#### Return Value

A CFDate object.

#### Discussion

The PDF specification defines a specific format for strings that represent dates. This function converts strings in that form to CFDate objects.

## Parameters

- `string`: The string to convert to a date.

## See Also

- [func CGPDFStringCopyTextString(CGPDFStringRef) -> CFString?](cgpdfstringcopytextstring(_:).md)
  Returns a CFString object that represents a PDF string as a text string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfstringcopydate(_:))*