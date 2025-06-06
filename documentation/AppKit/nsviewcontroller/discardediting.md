# discardEditing()

**Framework**: AppKit  
**Kind**: method

Causes the receiver to discard any changes, restoring the previous values.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func discardEditing()
```

## See Also

- [func commitEditing(withDelegate: Any?, didCommit: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsviewcontroller/commitediting(withdelegate:didcommit:contextinfo:).md)
  Attempt to commit any currently edited results of the receiver.
- [func commitEditing() -> Bool](nsviewcontroller/commitediting.md)
  Returns whether the receiver was able to commit any pending edits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/discardediting())*