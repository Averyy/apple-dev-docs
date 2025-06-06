# changeCount

**Framework**: AppKit  
**Kind**: property

The receiver’s change count.

**Availability**:
- macOS ?+

## Declaration

```swift
var changeCount: Int { get }
```

#### Discussion

The change count starts at zero when a client creates the receiver and becomes the first owner. The change count subsequently increments each time the pasteboard ownership changes.

The change count is also returned from [`clearContents()`](nspasteboard/clearcontents().md) and [`declareTypes(_:owner:)`](nspasteboard/declaretypes(_:owner:).md). You can therefore record the value of `changeCount` at the time that you take ownership of the pasteboard and compare it with a later value to determine whether you still have ownership.

## See Also

- [func clearContents() -> Int](nspasteboard/clearcontents.md)
  Clears the existing contents of the pasteboard.
- [func declareTypes([NSPasteboard.PasteboardType], owner: Any?) -> Int](nspasteboard/declaretypes(_:owner:).md)
  Prepares the receiver for a change in its contents by declaring the new types of data it will contain and a new owner.
- [var name: NSPasteboard.Name](nspasteboard/name-swift.property.md)
  The receiver’s name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/changecount)*