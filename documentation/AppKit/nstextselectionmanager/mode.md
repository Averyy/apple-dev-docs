# NSTextSelectionManager.Mode

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Values for text selection interaction modes.

**Availability**:
- macOS 27.0+

## Declaration

```swift
enum Mode
```

```c
enum NSTextSelectionMode : NSInteger;
```

#### Overview

These modes determine how the text selection manager handles user interaction with text content.

## Topics

### Enumeration Cases
- [NSTextSelectionManager.Mode.editable](./mode/editable.md)
  Text is editable and selectable.
- [NSTextSelectionManager.Mode.nonInteractive](./mode/noninteractive.md)
  Text is neither selectable nor editable.
- [NSTextSelectionManager.Mode.selectable](./mode/selectable.md)
  Text is selectable but not editable.
### Initializers
- [init?(rawValue: Int)](./mode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring text selection
- [var textSelectionMode: NSTextSelectionManager.Mode](./textselectionmode.md)
  The interaction mode for text selection.
- [var textSelectionDataSource: (any NSTextSelectionDataSource)?](./textselectiondatasource.md)
  The data source that provides text layout information to the selection manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectionmanager/mode)*