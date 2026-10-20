# setCurrentMediaItem(toItemAtIndex:)

**Framework**: TVMLKit  
**Kind**: method  
**Role**: Instance Method

Sets the current media item to the designated media item.

**Availability**:
- tvOS 12.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
func setCurrentMediaItem(toItemAtIndex index: Int)
```

```objc
- (void) changeToMediaItemAtIndex:(NSInteger) index;
```

## Parameters

- `index`: The location in the playlist array containing the desired media item.

## See Also

### Inspecting Media Items
- [var previousMediaItem: TVMediaItem?](./previousmediaitem.md)
  The previously selected media item.
- [var currentMediaItem: TVMediaItem?](./currentmediaitem.md)
  The currently selected media item.
- [var nextMediaItem: TVMediaItem?](./nextmediaitem.md)
  The next media item in the playlist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvplayer/setcurrentmediaitem(toitematindex:))*