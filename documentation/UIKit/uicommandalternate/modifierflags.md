# modifierFlags

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The bit mask of modifier keys that the user must press to invoke the action for the alternative command.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var modifierFlags: UIKeyModifierFlags { get }
```

```objc
@property (nonatomic, readonly) UIKeyModifierFlags modifierFlags;
```

## See Also

### Getting information about the alternative
- [var title: String](./title.md)
  The command alternative’s title.
- [var action: Selector](./action.md)
  The command alternative’s action-method selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicommandalternate/modifierflags)*