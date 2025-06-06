# systemButton(with:target:action:)

**Framework**: UIKit  
**Kind**: method

Creates and returns a system type button with specified image, target, and action.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func systemButton(with image: UIImage, target: Any?, action: Selector?) -> Self
```

#### Discussion

This method is a convenience constructor for creating a `UIButtonTypeSystem` type button objects with a specific target and action.

## Parameters

- `image`: The image for a system button.
- `target`: The object that receives the   message.
- `action`: The action to send to   when this item is selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/systembutton(with:target:action:))*