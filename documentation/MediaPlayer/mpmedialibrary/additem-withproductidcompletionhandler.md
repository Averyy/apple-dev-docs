# addItem(withProductID:completionHandler:)

**Framework**: Mediaplayer  
**Kind**: method

Adds the designated item to the user’s music library.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func addItem(withProductID productID: String) async throws -> [MPMediaEntity]
```

#### Discussion

Use this method to add media items to a user’s music library. Use the [`Apple Music API Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/AppleMusicWebServicesReference/index.html#//apple_ref/doc/uid/TP40017625) to search for content contained in the iTunes, App, Book, and Mac App stores.

> **Note**:  This method only works for 64-bit apps.

## Parameters

- `productID`: The product identifier for the media item to add.
- `completionHandler`: A block that the system calls after it plays the media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary/additem(withproductid:completionhandler:))*