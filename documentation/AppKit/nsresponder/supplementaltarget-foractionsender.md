# supplementalTarget(forAction:sender:)

**Framework**: AppKit  
**Kind**: method

Finds a target for an action method.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func supplementalTarget(forAction action: Selector, sender: Any?) -> Any?
```

#### Return Value

An object which responds to the action, or `nil`.

#### Discussion

If this `NSResponder` instance does not itself `respondsToSelector:`, then `supplementalTargetForAction:sender:` is called.

This method should return an object which responds to the action; if this responder does not have a supplemental object that does that, the implementation of this method should call `super`’s `supplementalTargetForAction:sender:`.

NSResponder’s implementation returns `nil`.

## Parameters

- `action`: The requested action.
- `sender`: The message sender.

## See Also

- [protocol NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
  Methods that responder subclasses implement to support key binding commands, such as inserting tabs and newlines, or moving the insertion point.
- [Action Messages](action-messages.md)
  Implement action messages in your first responders to handle common tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/supplementaltarget(foraction:sender:))*