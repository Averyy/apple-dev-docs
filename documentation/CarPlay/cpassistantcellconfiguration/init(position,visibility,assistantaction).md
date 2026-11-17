# init(position:visibility:assistantAction:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a configuration object with the specified position, visibility, and action.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
init(position: CPListItem.AssistantCellPosition, visibility: CPListItem.AssistantCellVisibility, assistantAction: CPAssistantCellActionType)
```

```objc
- (instancetype) initWithPosition:(CPAssistantCellPosition) position visibility:(CPAssistantCellVisibility) visibility assistantAction:(CPAssistantCellActionType) assistantAction;
```

## Return Value

A configuration object with the specified information.

## Discussion

Pass the object you receive from this method to your [`CPListTemplate`](../cplisttemplate.md) type, either at initialization time or by assigning it to the type’s [`assistantCellConfiguration`](../cplisttemplate/assistantcellconfiguration.md) property.

## Parameters

- `position`: The placement option within your list interface. For a list of possible values, see [`CPListItem.AssistantCellPosition`](../cplistitem/assistantcellposition.md).
- `visibility`: The visibility option for the assistant cell. You can display the cell at all times or only in specific situations. For a list of possible values, see [`CPListItem.AssistantCellVisibility`](../cplistitem/assistantcellvisibility.md).
- `assistantAction`: The type of action you want Siri to perform. CarPlay uses this value to determine which SiriKit intent to send to your app’s Intents extension. For a list of possible values, see [`CPAssistantCellActionType`](../cpassistantcellactiontype.md).

## See Also

### Creating an assistant cell configuration
- [init?(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpassistantcellconfiguration/init(position:visibility:assistantaction:))*