# init(position:visibility:assistantAction:)

**Framework**: CarPlay  
**Kind**: init

Creates a configuration object with the specified position, visibility, and action.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
init(position: CPListItem.AssistantCellPosition, visibility: CPListItem.AssistantCellVisibility, assistantAction: CPAssistantCellActionType)
```

#### Discussion

Your app doesn’t receive a callback when the user selects the assistant cell. Instead, you configure an Intents Extension to handle the type of intent you specify in `assistantAction`; audio apps must support [`INPlayMediaIntent`](https://developer.apple.com/documentation/Intents/INPlayMediaIntent) and communication apps must support [`INStartCallIntent`](https://developer.apple.com/documentation/Intents/INStartCallIntent). The assistant cell is unavailable in all other app categories.

## Parameters

- `position`: The position of the assistant cell in the list template. For possible values, see  .
- `visibility`: The visibility of the assistant cell. For possible values, see  .
- `assistantAction`: The action that Siri performs when the user selects the assistant cell. For possible values, see  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpassistantcellconfiguration/init(position:visibility:assistantaction:))*