# init(frame:primaryAction:)

**Framework**: UIKit  
**Kind**: init

Creates a new button with the specified frame, registers the primary action event, and sets the title and image to the action’s title and image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(frame: CGRect, primaryAction: UIAction?)
```

## Parameters

- `frame`: The frame rectangle for the view, measured in points.
- `primaryAction`: The action to perform when the button is selected. The button registers this action for the   control event and sets the title and image properties to the action’s title and image.

## See Also

- [init(frame: CGRect)](uibutton/init(frame:).md)
  Creates a new button with the specified frame.
- [init?(coder: NSCoder)](uibutton/init(coder:).md)
  Creates a new button with data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/init(frame:primaryaction:))*