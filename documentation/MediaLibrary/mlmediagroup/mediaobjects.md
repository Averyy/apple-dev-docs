# mediaObjects

**Framework**: Media Library  
**Kind**: property

A list of media objects in the media group.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+

## Declaration

```swift
var mediaObjects: [MLMediaObject]? { get }
```

#### Discussion

This accessor property is nonblocking. If there is no data yet, it returns `nil` and automatically triggers an internal asynchronous request. A KVO notification will be sent via the main thread when data arrives.

## See Also

- [var parent: MLMediaGroup?](mlmediagroup/parent.md)
  The media group’s parent group.
- [var childGroups: [MLMediaGroup]?](mlmediagroup/childgroups.md)
  A list of child groups contained in the media group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/mlmediagroup/mediaobjects)*