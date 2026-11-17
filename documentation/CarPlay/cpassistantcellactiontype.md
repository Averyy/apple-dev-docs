# CPAssistantCellActionType

**Framework**: CarPlay  
**Kind**: enum  
**Role**: Enumeration

The supported actions of the assistant cell.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
enum CPAssistantCellActionType
```

```c
enum CPAssistantCellActionType : NSInteger;
```

## Overview

The assistant cell supports a specific set of actions, and you use these constants to specify an action when configuring the cell. These actions require you to support SiriKit intents and support only audio, video, or communication apps.

## Topics

### Enumeration Cases
- [CPAssistantCellActionType.playMedia](./cpassistantcellactiontype/playmedia.md)
  An option to to play audio or video content.
- [CPAssistantCellActionType.startCall](./cpassistantcellactiontype/startcall.md)
  An option to call a person, group, or business.
### Initializers
- [init?(rawValue: Int)](./cpassistantcellactiontype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the configuration attributes
- [var assistantAction: CPAssistantCellActionType](./cpassistantcellconfiguration/assistantaction.md)
  The action that Siri performs when the user selects the assistant cell.
- [var position: CPListItem.AssistantCellPosition](./cpassistantcellconfiguration/position.md)
  The position of the assistant cell in the list template.
- [var visibility: CPListItem.AssistantCellVisibility](./cpassistantcellconfiguration/visibility.md)
  The visibility of the assistant cell in the list template.
- [CPListItem.AssistantCellPosition](./cplistitem/assistantcellposition.md)
  The supported placement options for the assistant cell.
- [CPListItem.AssistantCellVisibility](./cplistitem/assistantcellvisibility.md)
  The visibility options for the assistant cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpassistantcellactiontype)*