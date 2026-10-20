# childGroups

**Framework**: Media Library  
**Kind**: property  
**Role**: Instance Property

A list of child groups contained in the media group.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+ - Deprecated in 10.15

> **Deprecated**: MediaLibrary.framework will be removed in a future OS version. Use Photos.framework or iTunesLibrary.framework instead.

## Declaration

```swift
var childGroups: [MLMediaGroup]? { get }
```

```objc
@property (copy, readonly, nullable) NSArray<MLMediaGroup *> * childGroups;
```

## See Also

### Accessing the Group Hierarchy
- [var parent: MLMediaGroup?](./parent.md)
  The media group’s parent group.
- [var mediaObjects: [MLMediaObject]?](./mediaobjects.md)
  A list of media objects in the media group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/mlmediagroup/childgroups)*