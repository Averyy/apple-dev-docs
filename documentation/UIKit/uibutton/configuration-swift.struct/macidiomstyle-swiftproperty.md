# macIdiomStyle

**Framework**: UIKit  
**Kind**: property

The style to use when this button appears in macOS.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+

## Declaration

```swift
var macIdiomStyle: UIButton.Configuration.MacIdiomStyle { get set }
```

#### Discussion

Use this property when building your app with Mac Catalyst. The value [`UIButton.Configuration.MacIdiomStyle.automatic`](uibutton/configuration-swift.struct/macidiomstyle-swift.enum/automatic.md) lets the system choose the appropriate style. Select a specific style to force the button to always use that style.

## See Also

- [UIButton.Configuration.MacIdiomStyle](uibutton/configuration-swift.struct/macidiomstyle-swift.enum.md)
  The button style your app uses when running in macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/macidiomstyle-swift.property)*