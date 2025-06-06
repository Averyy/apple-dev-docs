# transliterateChinese(_:)

**Framework**: BrowserEngineKit  
**Kind**: method

Converts the selected text between traditional and simplified Chinese.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
optional func transliterateChinese(_ sender: Any?)
```

#### Overview

To invoke the standard operating system behavior for transliterating Chinese text, call [`transliterateChinese(forText:)`](betextinteraction/transliteratechinese(fortext:).md) in your implementation of this method.

When you change the selected text in your implementation of this method, notify the operating system by calling [`selectionWillChange(for:)`](betextinputdelegate/selectionwillchange(for:).md) and [`selectionDidChange(for:)`](betextinputdelegate/selectiondidchange(for:).md).

## See Also

- [func translate(Any?)](berespondereditactions/translate(_:).md)
  Presents a translation of the selected text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/berespondereditactions/transliteratechinese(_:))*