# assistantAction

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The action that Siri performs when the user selects the assistant cell.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var assistantAction: CPAssistantCellActionType { get }
```

```objc
@property (nonatomic, readonly) CPAssistantCellActionType assistantAction;
```

## Discussion

Specify the value of this property when creating the assistant cell configuration object. Actions require you to support SiriKit intents and support a implement a specific type of CarPlay app. For more information, see [`CPAssistantCellActionType`](../cpassistantcellactiontype.md).

## See Also

### Getting the configuration attributes
- [var position: CPListItem.AssistantCellPosition](./position.md)
  The position of the assistant cell in the list template.
- [var visibility: CPListItem.AssistantCellVisibility](./visibility.md)
  The visibility of the assistant cell in the list template.
- [enum CPAssistantCellActionType](../cpassistantcellactiontype.md)
  The supported actions of the assistant cell.
- [CPListItem.AssistantCellPosition](../cplistitem/assistantcellposition.md)
  The supported placement options for the assistant cell.
- [CPListItem.AssistantCellVisibility](../cplistitem/assistantcellvisibility.md)
  The visibility options for the assistant cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpassistantcellconfiguration/assistantaction)*