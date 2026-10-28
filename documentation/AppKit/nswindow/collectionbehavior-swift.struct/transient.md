# transient

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The window floats in Spaces and hides in Mission Control.

**Availability**:
- macOS 10.6+

## Declaration

```swift
static var transient: NSWindow.CollectionBehavior { get }
```

```c
NSWindowCollectionBehaviorTransient
```

## Discussion

This is the default behavior if `windowLevel` isn’t equal to [`normal`](../level-swift.struct/normal.md).

## See Also

### Spaces and Mission Control
- [static var managed: NSWindow.CollectionBehavior](./managed.md)
  The window participates in Mission Control and Spaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/collectionbehavior-swift.struct/transient)*