# init(frame:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a new button with the specified frame.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
init(frame: CGRect)
```

```objc
- (instancetype) initWithFrame:(CGRect) frame;
```

## Parameters

- `frame`: The frame rectangle for the view, measured in points.

## See Also

### Creating buttons
- [convenience init(frame: CGRect, primaryAction: UIAction?)](./init%28frame,primaryaction%29.md)
  Creates a new button with the specified frame, registers the primary action event, and sets the title and image to the action’s title and image.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a new button with data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/init(frame:))*