# didHintFocusMovement(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Indicates to the currently focused item that focus movement might occur.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
optional func didHintFocusMovement(_ hint: UIFocusMovementHint)
```

```objc
- (void) didHintFocusMovement:(UIFocusMovementHint *) hint;
```

## Discussion

The focus item is mutated by the focus engine whenever the user’s finger moves on the remote.

## Parameters

- `hint`: The movement hint object corresponding to the user’s input.

## See Also

### Providing movement hints
- [class UIFocusMovementHint](../uifocusmovementhint.md)
  Provides movement hint information for the focused item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusitem/didhintfocusmovement(_:))*