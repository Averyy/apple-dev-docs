# init(type:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates and returns a new button of the specified type.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
convenience init(type buttonType: UIButton.ButtonType)
```

```objc
+ (instancetype) buttonWithType:(UIButtonType) buttonType;
```

#### Return Value

A newly created button.

#### Discussion

This method is a convenience constructor for creating button objects with specific configurations.

When creating a custom button — a button with the type [`UIButton.ButtonType.custom`](./buttontype-swift.enum/custom.md) — the frame of the button is set to (`0`, `0`, `0`, `0`) initially. Before adding the button to your interface, you should update the frame to a more appropriate value.

## Parameters

- `buttonType`: The button type. See [`UIButton.ButtonType`](./buttontype-swift.enum.md) for the possible values.

## See Also

### Related Documentation
- [UIKit Catalog: Creating and customizing views and controls](../uikit-catalog-creating-and-customizing-views-and-controls.md)
  Customize your app’s user interface with views and controls.
### Creating buttons of a specific type
- [convenience init(type: UIButton.ButtonType, primaryAction: UIAction?)](./init%28type,primaryaction%29.md)
  Creates a new button with the specified type, registers the primary action event, and sets the title and image to the action’s title and image.
- [UIButton.ButtonType](./buttontype-swift.enum.md)
  Specifies the style of a button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/init(type:))*