# addItem(withProductID:completionHandler:)

**Framework**: Media Player  
**Kind**: method

Adds the item associated with the product identifier to the end of the playlist.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func addItem(withProductID productID: String) async throws
```

#### Discussion

The method adds a single media item associated with the product identifier to the playlist.

## Parameters

- `productID`: The product identifier for the item to add.
- `completionHandler`: A block that the system calls after it adds the item to the playlist.

## See Also

- [func add([MPMediaItem], completionHandler: (((any Error)?) -> Void)?)](mpmediaplaylist/add(_:completionhandler:).md)
  Adds an array of media items to the end of the playlist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylist/additem(withproductid:completionhandler:))*