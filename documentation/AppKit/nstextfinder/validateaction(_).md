# validateAction(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Allows validation of the find action before performing.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func validateAction(_ op: NSTextFinder.Action) -> Bool
```

```objc
- (BOOL) validateAction:(NSTextFinderAction) op;
```

#### Return Value

[`true`](../../Swift/true.md) if the operation is valid; otherwise [`false`](../../Swift/false.md).

#### Discussion

Responders the `NSResponder` method  [`performTextFinderAction(_:)`](../nsresponder/performtextfinderaction%28_%29.md) should call this method.

This method should be called by an implementation of [`validateUserInterfaceItem(_:)`](../nsuserinterfacevalidations/validateuserinterfaceitem%28_%29.md) to properly validate items with an action of [`performTextFinderAction(_:)`](../nsresponder/performtextfinderaction%28_%29.md). The responder’s [`validateUserInterfaceItem(_:)`](../nsuserinterfacevalidations/validateuserinterfaceitem%28_%29.md) or [`validateMenuItem:`](../../ObjectiveC/nsobject-swift.class/validatemenuitem_.md) implementation should pass the tag as the action for this method..

## Parameters

- `op`: The sender’s tag.

## See Also

### Validating and Performing Text Finding
- [func performAction(NSTextFinder.Action)](./performaction%28_%29.md)
  Performs the specified text finding action.
- [func cancelFindIndicator()](./cancelfindindicator%28%29.md)
  Cancels the find indicator immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinder/validateaction(_:))*