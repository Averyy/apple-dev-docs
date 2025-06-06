# performAction(_:)

**Framework**: AppKit  
**Kind**: method

Performs the specified text finding action.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func performAction(_ op: NSTextFinder.Action)
```

#### Discussion

Objects that respond to [`performTextFinderAction(_:)`](nsresponder/performtextfinderaction(_:).md) typically call [`validateAction(_:)`](nstextfinder/validateaction(_:).md) to ensure that the action is valid and then invoke [`performAction(_:)`](nstextfinder/performaction(_:).md) if validation is successful.

When invoking the [`validateAction(_:)`](nstextfinder/validateaction(_:).md) and [`performAction(_:)`](nstextfinder/performaction(_:).md) the item or sender’s tag should be passed as the parameter. By convention, the `sender` parameter for this method will have an [`NSTextFinder.Action`](nstextfinder/action.md) set as its tag. The responder that receives this method should pass the tag as the action for this method:

```objc
- (void)performTextFinderAction:(id)sender {
    [self.textFinder performAction:[sender tag]];
}
```

## Parameters

- `op`: The text finding action. See   for the possible values.

## See Also

- [func validateAction(NSTextFinder.Action) -> Bool](nstextfinder/validateaction(_:).md)
  Allows validation of the find action before performing.
- [func cancelFindIndicator()](nstextfinder/cancelfindindicator.md)
  Cancels the find indicator immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinder/performaction(_:))*