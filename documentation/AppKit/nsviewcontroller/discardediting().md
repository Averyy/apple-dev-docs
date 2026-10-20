# discardEditing()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Causes the receiver to discard any changes, restoring the previous values.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func discardEditing()
```

```objc
- (void) discardEditing;
```

## See Also

### NSEditor Conformance
- [func commitEditing(withDelegate: Any?, didCommit: Selector?, contextInfo: UnsafeMutableRawPointer?)](./commitediting%28withdelegate,didcommit,contextinfo%29.md)
  Attempt to commit any currently edited results of the receiver.
- [func commitEditing() -> Bool](./commitediting%28%29.md)
  Returns whether the receiver was able to commit any pending edits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/discardediting())*