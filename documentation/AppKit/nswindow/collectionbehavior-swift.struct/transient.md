# transient

**Framework**: AppKit  
**Kind**: property

The window floats in Spaces and hides in Mission Control.

**Availability**:
- macOS 10.6+

## Declaration

```swift
static var transient: NSWindow.CollectionBehavior { get }
```

#### Discussion

This is the default behavior if `windowLevel` isn’t equal to [`normal`](nswindow/level-swift.struct/normal.md).

## See Also

- [static var managed: NSWindow.CollectionBehavior](nswindow/collectionbehavior-swift.struct/managed.md)
  The window participates in Mission Control and Spaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/collectionbehavior-swift.struct/transient)*