# init(frame:primaryAction:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a new button with the specified frame, registers the primary action event, and sets the title and image to the action’s title and image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(frame: CGRect, primaryAction: UIAction?)
```

```objc
- (instancetype) initWithFrame:(CGRect) frame primaryAction:(UIAction *) primaryAction;
```

## Parameters

- `frame`: The frame rectangle for the view, measured in points.
- `primaryAction`: The action to perform when the button is selected. The button registers this action for the [`primaryActionTriggered`](../uicontrol/event/primaryactiontriggered.md) control event and sets the title and image properties to the action’s title and image.

## See Also

### Creating buttons
- [init(frame: CGRect)](./init%28frame%29.md)
  Creates a new button with the specified frame.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a new button with data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/init(frame:primaryaction:))*