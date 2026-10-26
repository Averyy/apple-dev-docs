# systemButtonWithPrimaryAction:

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates and returns a system type button, registers the primary action event, and sets the title and image to the action’s title and image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) systemButtonWithPrimaryAction:(UIAction *) primaryAction;
```

## Parameters

- `primaryAction`: The action to perform when the button is selected. The button registers this action for the [`primaryActionTriggered`](../uicontrol/event/primaryactiontriggered.md) control event and sets the title and image properties to the action’s title and image.

## See Also

### Creating system buttons
- [class func systemButton(with: UIImage, target: Any?, action: Selector?) -> Self](./systembutton%28with,target,action%29.md)
  Creates and returns a system type button with specified image, target, and action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/systembuttonwithprimaryaction:)*