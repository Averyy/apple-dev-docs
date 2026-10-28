# textField

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The text field that the scrubber item uses to display its text.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
var textField: NSTextField { get }
```

```objc
@property (strong, readonly) NSTextField * textField;
```

## Discussion

Access and configure the underlying text field used to display the text in the [`title`](./title.md) property.

## See Also

### Providing text content
- [var title: String](./title.md)
  The text displayed for the scrubber item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubbertextitemview/textfield)*