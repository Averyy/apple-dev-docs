# image

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The key command’s image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var image: UIImage? { get set }
```

```objc
@property (nonatomic, copy, nullable) UIImage * image;
```

#### Discussion

Only the [`context`](../uimenusystem/context.md) command system supports the display of an image, and only when the app is running in iOS.

## See Also

### Getting information about the key command
- [var title: String](./title.md)
  The key command’s title.
- [var input: String?](./input.md)
  The string of characters corresponding to the keys that must be pressed to match this key command.
- [var action: Selector?](./action.md)
  The command’s action-method selector.
- [var modifierFlags: UIKeyModifierFlags](./modifierflags.md)
  The bit mask of modifier flags that must be pressed to match this key command.
- [struct UIKeyModifierFlags](../uikeymodifierflags.md)
  Constants that indicate which modifier keys are pressed.
- [var discoverabilityTitle: String?](./discoverabilitytitle.md)
  An elaborated title that explains the purpose of the key command.
- [var attributes: UIMenuElement.Attributes](./attributes.md)
  The attributes indicating the style of the key command.
- [var state: UIMenuElement.State](./state.md)
  The state of the key command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uikeycommand/image)*