# mediaSources

**Framework**: Media Library  
**Kind**: property  
**Role**: Instance Property

Returns a dictionary of media sources by identifier.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+ - Deprecated in 10.15

> **Deprecated**: MediaLibrary.framework will be removed in a future OS version. Use Photos.framework or iTunesLibrary.framework instead.

## Declaration

```swift
var mediaSources: [String : MLMediaSource]? { get }
```

```objc
@property (copy, readonly, nullable) NSDictionary<NSString *,MLMediaSource *> * mediaSources;
```

#### Discussion

Returns `nil` the first time, beginning an asynchronous load of the media sources. A KVO notification is sent when all media sources have been loaded. If there are no objects in a media source, the source does not appear in this dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/mlmedialibrary/mediasources)*