# parent

**Framework**: Media Library  
**Kind**: property  
**Role**: Instance Property

The media group’s parent group.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+ - Deprecated in 10.15

> **Deprecated**: MediaLibrary.framework will be removed in a future OS version. Use Photos.framework or iTunesLibrary.framework instead.

## Declaration

```swift
unowned(unsafe) var parent: MLMediaGroup? { get }
```

```objc
@property (assign, readonly, nullable) MLMediaGroup * parent;
```

## See Also

### Accessing the Group Hierarchy
- [var childGroups: [MLMediaGroup]?](./childgroups.md)
  A list of child groups contained in the media group.
- [var mediaObjects: [MLMediaObject]?](./mediaobjects.md)
  A list of media objects in the media group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/mlmediagroup/parent)*