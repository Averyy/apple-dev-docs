# init(type:primaryAction:)

**Framework**: UIKit  
**Kind**: init

Creates a new button with the specified type, registers the primary action event, and sets the title and image to the action’s title and image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(type buttonType: UIButton.ButtonType = .system, primaryAction: UIAction?)
```

## Parameters

- `buttonType`: The type of button.
- `primaryAction`: The action to perform when the button is selected. The button registers this action for the   control event and sets the title and image properties to the action’s title and image.

## See Also

- [convenience init(type: UIButton.ButtonType)](uibutton/init(type:).md)
  Creates and returns a new button of the specified type.
- [UIButton.ButtonType](uibutton/buttontype-swift.enum.md)
  Specifies the style of a button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/init(type:primaryaction:))*