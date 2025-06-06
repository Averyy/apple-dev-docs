# add(_:completionHandler:)

**Framework**: Media Player  
**Kind**: method

Adds an array of media items to the end of the playlist.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func add(_ mediaItems: [MPMediaItem]) async throws
```

## Parameters

- `mediaItems`: The array of media items to add to the end of the playlist.
- `completionHandler`: A block that the system calls after it adds the media items to the playlist.

## See Also

- [func addItem(withProductID: String, completionHandler: (((any Error)?) -> Void)?)](mpmediaplaylist/additem(withproductid:completionhandler:).md)
  Adds the item associated with the product identifier to the end of the playlist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylist/add(_:completionhandler:))*