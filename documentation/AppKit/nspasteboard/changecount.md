# changeCount

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s change count.

**Availability**:
- macOS

## Declaration

```swift
var changeCount: Int { get }
```

```objc
@property (readonly) NSInteger changeCount;
```

#### Discussion

The change count starts at zero when a client creates the receiver and becomes the first owner. The change count subsequently increments each time the pasteboard ownership changes.

The change count is also returned from [`clearContents()`](./clearcontents%28%29.md) and [`declareTypes(_:owner:)`](./declaretypes%28_,owner%29.md). You can therefore record the value of `changeCount` at the time that you take ownership of the pasteboard and compare it with a later value to determine whether you still have ownership.

## See Also

### Related Documentation
- [func clearContents() -> Int](./clearcontents%28%29.md)
  Clears the existing contents of the pasteboard.
- [func declareTypes([NSPasteboard.PasteboardType], owner: Any?) -> Int](./declaretypes%28_,owner%29.md)
  Prepares the receiver for a change in its contents by declaring the new types of data it will contain and a new owner.
### Getting information about a pasteboard
- [var name: NSPasteboard.Name](./name-swift.property.md)
  The receiver’s name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/changecount)*