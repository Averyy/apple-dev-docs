# CPListItem.AssistantCellPosition

**Framework**: CarPlay  
**Kind**: enum  
**Role**: Enumeration

The supported placement options for the assistant cell.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
enum AssistantCellPosition
```

```c
enum CPAssistantCellPosition : NSInteger;
```

## Overview

The assistant cell supports a specific set of placement options, and you use these constants to indicate whether to place the cell before or after your app’s content.

## Topics

### Enumeration Cases
- [CPListItem.AssistantCellPosition.bottom](./assistantcellposition/bottom.md)
  An option to place the assistant cell above all visible cells in your list template.
- [CPListItem.AssistantCellPosition.top](./assistantcellposition/top.md)
  An option to place the assistant cell below all visible cells in your list template.
### Initializers
- [init?(rawValue: Int)](./assistantcellposition/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the configuration attributes
- [var assistantAction: CPAssistantCellActionType](../cpassistantcellconfiguration/assistantaction.md)
  The action that Siri performs when the user selects the assistant cell.
- [var position: CPListItem.AssistantCellPosition](../cpassistantcellconfiguration/position.md)
  The position of the assistant cell in the list template.
- [var visibility: CPListItem.AssistantCellVisibility](../cpassistantcellconfiguration/visibility.md)
  The visibility of the assistant cell in the list template.
- [enum CPAssistantCellActionType](../cpassistantcellactiontype.md)
  The supported actions of the assistant cell.
- [CPListItem.AssistantCellVisibility](./assistantcellvisibility.md)
  The visibility options for the assistant cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/assistantcellposition)*