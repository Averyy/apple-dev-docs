# NSTextSelectionManager.Mode

**Framework**: AppKit  
**Kind**: enum

Values for text selection interaction modes.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
enum Mode
```

#### Overview

These modes determine how the text selection manager handles user interaction with text content.

## Topics

### Enumeration Cases
- [NSTextSelectionManager.Mode.editable](nstextselectionmanager/mode/editable.md)
  Text is editable and selectable.
- [NSTextSelectionManager.Mode.nonInteractive](nstextselectionmanager/mode/noninteractive.md)
  Text is neither selectable nor editable.
- [NSTextSelectionManager.Mode.selectable](nstextselectionmanager/mode/selectable.md)
  Text is selectable but not editable.
### Initializers
- [init?(rawValue: Int)](nstextselectionmanager/mode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var textSelectionMode: NSTextSelectionManager.Mode](nstextselectionmanager/textselectionmode.md)
  The interaction mode for text selection.
- [var textSelectionDataSource: (any NSTextSelectionDataSource)?](nstextselectionmanager/textselectiondatasource.md)
  The data source that provides text layout information to the selection manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectionmanager/mode)*