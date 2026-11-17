# CPListItem.AssistantCellVisibility

**Framework**: CarPlay  
**Kind**: enum  
**Role**: Enumeration

The visibility options for the assistant cell.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
enum AssistantCellVisibility
```

```c
enum CPAssistantCellVisibility : NSInteger;
```

## Overview

Specify when you want the assistant cell to be visible from your list interface. You can show or hide the cell at all times, or enable it only at relevant moments.

## Topics

### Enumeration Cases
- [CPListItem.AssistantCellVisibility.always](./assistantcellvisibility/always.md)
  An option to always show the assistant cell.
- [CPListItem.AssistantCellVisibility.off](./assistantcellvisibility/off.md)
  An option to hide the assistant cell.
- [CPListItem.AssistantCellVisibility.whileLimitedUIActive](./assistantcellvisibility/whilelimiteduiactive.md)
  An option to show the assistant cell only when Limited UI mode is active.
### Initializers
- [init?(rawValue: Int)](./assistantcellvisibility/init%28rawvalue%29.md)

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
- [CPListItem.AssistantCellPosition](./assistantcellposition.md)
  The supported placement options for the assistant cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/assistantcellvisibility)*