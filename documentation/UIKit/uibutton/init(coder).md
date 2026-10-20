# init(coder:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a new button with data in an unarchiver.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
init?(coder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) coder;
```

## Parameters

- `coder`: An unarchiver object.

## See Also

### Creating buttons
- [init(frame: CGRect)](./init%28frame%29.md)
  Creates a new button with the specified frame.
- [convenience init(frame: CGRect, primaryAction: UIAction?)](./init%28frame,primaryaction%29.md)
  Creates a new button with the specified frame, registers the primary action event, and sets the title and image to the action’s title and image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/init(coder:))*