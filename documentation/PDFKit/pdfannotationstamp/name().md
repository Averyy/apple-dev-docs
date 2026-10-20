# name()

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Returns name associated with the stamp annotation.

**Availability**:
- macOS 10.5+ - Deprecated in 10.12

## Declaration

```swift
func name() -> String!
```

```objc
- (NSString *) name;
```

#### Discussion

Note that the name value of the stamp annotation is not necessarily identical to the user-visible appearance of the stamp annotation. For example, a stamp annotation that displays “Confidential” on a PDF page may not have a name value of “Confidential”.

## See Also

### Accessing and setting the stamp annotation
- [func setName(String!)](./setname%28_%29.md)
  Sets the name associated with the stamp annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationstamp/name())*