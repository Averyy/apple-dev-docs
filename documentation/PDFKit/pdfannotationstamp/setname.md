# setName(_:)

**Framework**: PDFKit  
**Kind**: method

Sets the name associated with the stamp annotation.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func setName(_ name: String!)
```

#### Discussion

The name must be representable in ASCII. You can set a stamp annotation’s name to help you identify it, but that name is not displayed on the PDF page. You must provide the string you want displayed on the page, such as “Draft” or “Top Secret”, in the appearance stream for the annotation.

## See Also

- [func name() -> String!](pdfannotationstamp/name.md)
  Returns name associated with the stamp annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationstamp/setname(_:))*