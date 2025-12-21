# commitEditing()

**Framework**: AppKit  
**Kind**: method

Returns whether the receiver was able to commit any pending edits.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func commitEditing() -> Bool
```

#### Return Value

Returns [`true`](https://developer.apple.com/documentation/Swift/true) if the changes were successfully applied to the model, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

#### Discussion

A commit is denied if the receiver fails to apply the changes to the model object, perhaps due to a validation error.

## See Also

- [func commitEditing(withDelegate: Any?, didCommit: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsviewcontroller/commitediting(withdelegate:didcommit:contextinfo:).md)
  Attempt to commit any currently edited results of the receiver.
- [func discardEditing()](nsviewcontroller/discardediting.md)
  Causes the receiver to discard any changes, restoring the previous values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/commitediting())*