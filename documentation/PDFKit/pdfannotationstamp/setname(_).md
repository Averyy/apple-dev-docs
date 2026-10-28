# setName(_:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Sets the name associated with the stamp annotation.

**Availability**:
- macOS 10.5+ - Deprecated in 10.12

## Declaration

```swift
func setName(_ name: String!)
```

```objc
- (void) setName:(NSString *) name;
```

## Discussion

The name must be representable in ASCII. You can set a stamp annotation’s name to help you identify it, but that name is not displayed on the PDF page. You must provide the string you want displayed on the page, such as “Draft” or “Top Secret”, in the appearance stream for the annotation.

## See Also

### Accessing and setting the stamp annotation
- [func name() -> String!](./name%28%29.md)
  Returns name associated with the stamp annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationstamp/setname(_:))*