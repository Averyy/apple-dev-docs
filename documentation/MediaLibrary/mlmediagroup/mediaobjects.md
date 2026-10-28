# mediaObjects

**Framework**: Media Library  
**Kind**: property  
**Role**: Instance Property

A list of media objects in the media group.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+ - Deprecated in 10.15

> **Deprecated**: MediaLibrary.framework will be removed in a future OS version. Use Photos.framework or iTunesLibrary.framework instead.

## Declaration

```swift
var mediaObjects: [MLMediaObject]? { get }
```

```objc
@property (copy, readonly, nullable) NSArray<MLMediaObject *> * mediaObjects;
```

## Discussion

This accessor property is nonblocking. If there is no data yet, it returns `nil` and automatically triggers an internal asynchronous request. A KVO notification will be sent via the main thread when data arrives.

## See Also

### Accessing the Group Hierarchy
- [var parent: MLMediaGroup?](./parent.md)
  The media group’s parent group.
- [var childGroups: [MLMediaGroup]?](./childgroups.md)
  A list of child groups contained in the media group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/mlmediagroup/mediaobjects)*