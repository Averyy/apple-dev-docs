# automatic

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The default text field style, based on the text field’s context.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@export(implementation)
static var automatic: DefaultTextFieldStyle { get }
```

Available when `Self` is `DefaultTextFieldStyle`.

## Discussion

The default style represents the recommended style based on the current platform and the text field’s context within the view hierarchy.

## See Also

### Getting built-in text field styles
- [static var bordered: BorderedTextFieldStyle](./bordered.md)
  A text field style with a system-defined border whose shape is determined by the [`textInputBorderShape(_:)`](../view/textinputbordershape%28_%29.md) modifier.
- [static var plain: PlainTextFieldStyle](./plain.md)
  A text field style with no decoration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfieldstyle/automatic)*