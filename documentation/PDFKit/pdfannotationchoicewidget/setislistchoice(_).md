# setIsListChoice(_:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Sets whether the widget annotation is a list.

**Availability**:
- macOS 10.4+ - Deprecated in 10.12

## Declaration

```swift
func setIsListChoice(_ isList: Bool)
```

```objc
- (void) setIsListChoice:(BOOL) isList;
```

## Discussion

A choice widget annotation can be either a list or a pop-up menu.

## Parameters

- `isList`: Send [`true`](../../Swift/true.md) to set the choice widget annotation is a list, [`false`](../../Swift/false.md) otherwise.

## See Also

### Determining the Type of Choice Widget Annotation
- [func isListChoice() -> Bool](./islistchoice%28%29.md)
  Returns a Boolean value indicating whether the widget annotation is a list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationchoicewidget/setislistchoice(_:))*