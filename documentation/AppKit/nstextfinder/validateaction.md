# validateAction(_:)

**Framework**: AppKit  
**Kind**: method

Allows validation of the find action before performing.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func validateAction(_ op: NSTextFinder.Action) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the operation is valid; otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

Responders the `NSResponder` method  [`performTextFinderAction(_:)`](nsresponder/performtextfinderaction(_:).md) should call this method.

This method should be called by an implementation of [`validateUserInterfaceItem(_:)`](nsuserinterfacevalidations/validateuserinterfaceitem(_:).md) to properly validate items with an action of [`performTextFinderAction(_:)`](nsresponder/performtextfinderaction(_:).md). The responder’s [`validateUserInterfaceItem(_:)`](nsuserinterfacevalidations/validateuserinterfaceitem(_:).md) or [`validateMenuItem:`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/validateMenuItem:) implementation should pass the tag as the action for this method..

## Parameters

- `op`: The sender’s tag.

## See Also

- [func performAction(NSTextFinder.Action)](nstextfinder/performaction(_:).md)
  Performs the specified text finding action.
- [func cancelFindIndicator()](nstextfinder/cancelfindindicator.md)
  Cancels the find indicator immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinder/validateaction(_:))*