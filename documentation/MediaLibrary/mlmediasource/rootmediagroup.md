# rootMediaGroup

**Framework**: Media Library  
**Kind**: property

The base media group in the media source that contains all other groups within the source as descendant elements.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+

## Declaration

```swift
var rootMediaGroup: MLMediaGroup? { get }
```

#### Discussion

This accessor property is nonblocking. If there is no data yet, it returns `nil` and automatically triggers an internal asynchronous request. When data arrives, a KVO notification is sent via the main thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/mlmediasource/rootmediagroup)*