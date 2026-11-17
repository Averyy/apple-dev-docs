# delegate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An object that customizes presentation of the menu and actions to display for an edit menu interaction.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any UIEditMenuInteractionDelegate)? { get }
```

```objc
@property (nonatomic, weak, readonly, nullable) id<UIEditMenuInteractionDelegate> delegate;
```

## See Also

### Responding to menu requests
- [protocol UIEditMenuInteractionDelegate](../uieditmenuinteractiondelegate.md)
  The methods for customizing the menu the interaction displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uieditmenuinteraction/delegate)*