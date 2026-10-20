# setChoices(_:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Sets the items available in the list or pop-up menu of the choice widget annotation.

**Availability**:
- macOS 10.4+ - Deprecated in 10.12

## Declaration

```swift
func setChoices(_ options: [Any]!)
```

```objc
- (void) setChoices:(NSArray *) options;
```

## Parameters

- `options`: Send an array of strings, each of which represents an item in the list or pop-up menu of the choice annotation widget.

## See Also

### Accessing the Items in the Choice Widget Annotation
- [func choices() -> [Any]!](./choices%28%29.md)
  Returns an array of strings that represent the items available in the list or pop-up menu of the choice widget annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationchoicewidget/setchoices(_:))*