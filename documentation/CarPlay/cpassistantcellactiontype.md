# CPAssistantCellActionType

**Framework**: CarPlay  
**Kind**: enum  
**Role**: Enumeration

The supported Siri actions of the assistant cell.

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

## Topics

### Siri Actions
- [CPAssistantCellActionType.playMedia](./cpassistantcellactiontype/playmedia.md)
  Provides an action that uses Siri to prompt the user for media playback.
- [CPAssistantCellActionType.startCall](./cpassistantcellactiontype/startcall.md)
  Provides an action that uses Siri to prompt the user for a person, group, or business to call.
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

### Getting the Configuration Attributes
- [var position: CPListItem.AssistantCellPosition](./cpassistantcellconfiguration/position.md)
  The position of the assistant cell in the list template.
- [var visibility: CPListItem.AssistantCellVisibility](./cpassistantcellconfiguration/visibility.md)
  The visibility of the assistant cell in the list template.
- [var assistantAction: CPAssistantCellActionType](./cpassistantcellconfiguration/assistantaction.md)
  The action that Siri performs when the user selects the assistant cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpassistantcellactiontype)*