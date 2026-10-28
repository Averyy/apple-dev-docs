# commitEditing()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns whether the receiver was able to commit any pending edits.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func commitEditing() -> Bool
```

```objc
- (BOOL) commitEditing;
```

## Return Value

Returns [`true`](../../Swift/true.md) if the changes were successfully applied to the model, [`false`](../../Swift/false.md) otherwise.

## Discussion

A commit is denied if the receiver fails to apply the changes to the model object, perhaps due to a validation error.

## See Also

### NSEditor Conformance
- [func commitEditing(withDelegate: Any?, didCommit: Selector?, contextInfo: UnsafeMutableRawPointer?)](./commitediting%28withdelegate,didcommit,contextinfo%29.md)
  Attempt to commit any currently edited results of the receiver.
- [func discardEditing()](./discardediting%28%29.md)
  Causes the receiver to discard any changes, restoring the previous values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/commitediting())*