# managed

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The window participates in Mission Control and Spaces.

**Availability**:
- macOS 10.6+

## Declaration

```swift
static var managed: NSWindow.CollectionBehavior { get }
```

```c
NSWindowCollectionBehaviorManaged
```

#### Discussion

This is the default behavior if `windowLevel` is equal to [`normal`](../level-swift.struct/normal.md).

## See Also

### Spaces and Mission Control
- [static var transient: NSWindow.CollectionBehavior](./transient.md)
  The window floats in Spaces and hides in Mission Control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/collectionbehavior-swift.struct/managed)*