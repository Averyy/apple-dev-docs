# addItem(withProductID:completionHandler:)

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

Adds the item associated with the product identifier to the end of the playlist.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func addItem(withProductID productID: String, completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
func addItem(withProductID productID: String) async throws
```

```objc
- (void) addItemWithProductID:(NSString *) productID completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Discussion

The method adds a single media item associated with the product identifier to the playlist.

## Parameters

- `productID`: The product identifier for the item to add.
- `completionHandler`: A block that the system calls after it adds the item to the playlist.

  - **error**: If an error occurred, this parameter holds the error object that explains the error. Otherwise, the value of this parameter is [`nil`](../../ObjectiveC/nil-227m0.md).

## See Also

### Adding media items to a playlist
- [func add([MPMediaItem], completionHandler: (((any Error)?) -> Void)?)](./add%28_,completionhandler%29.md)
  Adds an array of media items to the end of the playlist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylist/additem(withproductid:completionhandler:))*