# currentMediaItem

**Framework**: TVMLKit  
**Kind**: property  
**Role**: Instance Property

The currently selected media item.

**Availability**:
- tvOS 12.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
var currentMediaItem: TVMediaItem? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) TVMediaItem * currentMediaItem;
```

## See Also

### Inspecting Media Items
- [func setCurrentMediaItem(toItemAtIndex: Int)](./setcurrentmediaitem%28toitematindex%29.md)
  Sets the current media item to the designated media item.
- [var previousMediaItem: TVMediaItem?](./previousmediaitem.md)
  The previously selected media item.
- [var nextMediaItem: TVMediaItem?](./nextmediaitem.md)
  The next media item in the playlist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvplayer/currentmediaitem)*