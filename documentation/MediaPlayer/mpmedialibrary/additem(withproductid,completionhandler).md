# addItem(withProductID:completionHandler:)

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

Adds the designated item to the user’s music library.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func addItem(withProductID productID: String, completionHandler: (@Sendable ([MPMediaEntity], (any Error)?) -> Void)? = nil)
```

```swift
func addItem(withProductID productID: String) async throws -> [MPMediaEntity]
```

```objc
- (void) addItemWithProductID:(NSString *) productID completionHandler:(void (^)(NSArray<__kindof MPMediaEntity *> *entities, NSError *error)) completionHandler;
```

#### Discussion

Use this method to add media items to a user’s music library. Use the [Apple Music API Reference](https://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/AppleMusicWebServicesReference/index.html#//apple_ref/doc/uid/TP40017625) to search for content contained in the iTunes, App, Book, and Mac App stores.

> **Note**:  This method only works for 64-bit apps.

## Parameters

- `productID`: The product identifier for the media item to add.
- `completionHandler`: A block that the system calls after it plays the media item.

  - **entities**: An array containing the media items added to the user’s music library.
  - **error**: If an error occurred, this parameter holds the error object that explains the error. Otherwise, the value of this parameter is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary/additem(withproductid:completionhandler:))*