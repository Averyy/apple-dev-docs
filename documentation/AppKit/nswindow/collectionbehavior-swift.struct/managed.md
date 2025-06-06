# managed

**Framework**: AppKit  
**Kind**: property

The window participates in Mission Control and Spaces.

**Availability**:
- macOS 10.6+

## Declaration

```swift
static var managed: NSWindow.CollectionBehavior { get }
```

#### Discussion

This is the default behavior if `windowLevel` is equal to [`normal`](nswindow/level-swift.struct/normal.md).

## See Also

- [static var transient: NSWindow.CollectionBehavior](nswindow/collectionbehavior-swift.struct/transient.md)
  The window floats in Spaces and hides in Mission Control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/collectionbehavior-swift.struct/managed)*