# rootMediaGroup

**Framework**: Media Library  
**Kind**: property  
**Role**: Instance Property

The base media group in the media source that contains all other groups within the source as descendant elements.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+ - Deprecated in 10.15

> **Deprecated**: MediaLibrary.framework will be removed in a future OS version. Use Photos.framework or iTunesLibrary.framework instead.

## Declaration

```swift
var rootMediaGroup: MLMediaGroup? { get }
```

```objc
@property (retain, readonly, nullable) MLMediaGroup * rootMediaGroup;
```

## Discussion

This accessor property is nonblocking. If there is no data yet, it returns `nil` and automatically triggers an internal asynchronous request. When data arrives, a KVO notification is sent via the main thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/mlmediasource/rootmediagroup)*