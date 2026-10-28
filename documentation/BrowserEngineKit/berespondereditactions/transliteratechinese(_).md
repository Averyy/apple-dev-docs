# transliterateChinese(_:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) transliterateChinese:(id) sender;
```

## Discussion

To invoke the standard system behavior for transliterating Chinese text, call [`transliterateChinese(forText:)`](../betextinteraction/transliteratechinese%28fortext%29.md) in your implementation of this method.

When you change the selected text in your implementation of this method, notify the system by calling [`selectionWillChange(for:)`](../betextinputdelegate/selectionwillchange%28for%29.md) and [`selectionDidChange(for:)`](../betextinputdelegate/selectiondidchange%28for%29.md).

## See Also

### Translating and transliterating text
- [func translate(Any?)](./translate%28_%29.md)
  Presents a translation of the selected text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/berespondereditactions/transliteratechinese(_:))*