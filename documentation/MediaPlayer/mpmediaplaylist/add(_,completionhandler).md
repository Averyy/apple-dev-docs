# add(_:completionHandler:)

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

Adds an array of media items to the end of the playlist.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func add(_ mediaItems: [MPMediaItem], completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
func add(_ mediaItems: [MPMediaItem]) async throws
```

```objc
- (void) addMediaItems:(NSArray<MPMediaItem *> *) mediaItems completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Parameters

- `mediaItems`: The array of media items to add to the end of the playlist.
- `completionHandler`: A block that the system calls after it adds the media items to the playlist.

  - **error**: If an error occurred, this parameter holds the error object that explains the error. Otherwise, the value of this parameter is [`nil`](../../ObjectiveC/nil-227m0.md).

## See Also

### Adding media items to a playlist
- [func addItem(withProductID: String, completionHandler: (((any Error)?) -> Void)?)](./additem%28withproductid,completionhandler%29.md)
  Adds the item associated with the product identifier to the end of the playlist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylist/add(_:completionhandler:))*