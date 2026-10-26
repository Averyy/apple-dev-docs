# buttonWithType:primaryAction:

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a new button with the specified type, registers the primary action event, and sets the title and image to the action’s title and image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) buttonWithType:(UIButtonType) buttonType primaryAction:(UIAction *) primaryAction;
```

## Parameters

- `buttonType`: The type of button.
- `primaryAction`: The action to perform when the button is selected. The button registers this action for the [`primaryActionTriggered`](../uicontrol/event/primaryactiontriggered.md) control event and sets the title and image properties to the action’s title and image.

## See Also

### Creating buttons of a specific type
- [convenience init(type: UIButton.ButtonType)](./init%28type%29.md)
  Creates and returns a new button of the specified type.
- [UIButton.ButtonType](./buttontype-swift.enum.md)
  Specifies the style of a button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/buttonwithtype:primaryaction:)*