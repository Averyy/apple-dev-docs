# performAction(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Performs the specified text finding action.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func performAction(_ op: NSTextFinder.Action)
```

```objc
- (void) performAction:(NSTextFinderAction) op;
```

## Discussion

Objects that respond to [`performTextFinderAction(_:)`](../nsresponder/performtextfinderaction%28_%29.md) typically call [`validateAction(_:)`](./validateaction%28_%29.md) to ensure that the action is valid and then invoke [`performAction(_:)`](./performaction%28_%29.md) if validation is successful.

When invoking the [`validateAction(_:)`](./validateaction%28_%29.md) and [`performAction(_:)`](./performaction%28_%29.md) the item or sender’s tag should be passed as the parameter. By convention, the `sender` parameter for this method will have an [`NSTextFinder.Action`](./action.md) set as its tag. The responder that receives this method should pass the tag as the action for this method:

```objc
- (void)performTextFinderAction:(id)sender {
    [self.textFinder performAction:[sender tag]];
}
```

## Parameters

- `op`: The text finding action. See [`NSTextFinder.Action`](./action.md) for the possible values.

## See Also

### Validating and Performing Text Finding
- [func validateAction(NSTextFinder.Action) -> Bool](./validateaction%28_%29.md)
  Allows validation of the find action before performing.
- [func cancelFindIndicator()](./cancelfindindicator%28%29.md)
  Cancels the find indicator immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinder/performaction(_:))*