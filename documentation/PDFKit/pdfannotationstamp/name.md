# name()

**Framework**: PDFKit  
**Kind**: method

Returns name associated with the stamp annotation.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func name() -> String!
```

#### Discussion

Note that the name value of the stamp annotation is not necessarily identical to the user-visible appearance of the stamp annotation. For example, a stamp annotation that displays “Confidential” on a PDF page may not have a name value of “Confidential”.

## See Also

- [func setName(String!)](pdfannotationstamp/setname(_:).md)
  Sets the name associated with the stamp annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationstamp/name())*