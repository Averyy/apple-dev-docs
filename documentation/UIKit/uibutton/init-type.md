# init(type:)

**Framework**: UIKit  
**Kind**: init

Creates and returns a new button of the specified type.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(type buttonType: UIButton.ButtonType)
```

#### Return Value

A newly created button.

#### Discussion

This method is a convenience constructor for creating button objects with specific configurations.

When creating a custom button — a button with the type [`UIButton.ButtonType.custom`](uibutton/buttontype-swift.enum/custom.md) — the frame of the button is set to (`0`, `0`, `0`, `0`) initially. Before adding the button to your interface, you should update the frame to a more appropriate value.

## Parameters

- `buttonType`: The button type. See   for the possible values.

## See Also

- [UIKit Catalog: Creating and customizing views and controls](uikit-catalog-creating-and-customizing-views-and-controls.md)
  Customize your app’s user interface with views and controls.
- [convenience init(type: UIButton.ButtonType, primaryAction: UIAction?)](uibutton/init(type:primaryaction:).md)
  Creates a new button with the specified type, registers the primary action event, and sets the title and image to the action’s title and image.
- [UIButton.ButtonType](uibutton/buttontype-swift.enum.md)
  Specifies the style of a button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/init(type:))*