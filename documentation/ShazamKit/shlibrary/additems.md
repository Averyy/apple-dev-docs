# addItems(_:)

**Framework**: ShazamKit  
**Kind**: method

Adds an array of media items to the user’s Shazam library.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
final func addItems(_ items: [SHMediaItem]) async throws
```

#### Discussion

The library only accepts media items with a [`shazamID`](shmediaitem/shazamid.md). The `shazamID` must be a numeric only string.

This throws [`SHError.Code.mediaLibrarySyncFailed`](sherror/code/medialibrarysyncfailed.md) if the system can’t add at least one [`SHMediaItem`](shmediaitem.md) or if an error occurred during the addition. In that case, the system doesn’t add any items to the library.

## Parameters

- `items`: An array containing the   objects to add to the library.

## See Also

- [static let `default`: SHLibrary](shlibrary/default.md)
  An instance of the default Shazam library.
- [func removeItems([SHMediaItem]) async throws](shlibrary/removeitems(_:).md)
  Removes an array of media items from the user’s Shazam library.
- [var items: [SHMediaItem]](shlibrary/items.md)
  The list of synced items in the Media Library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shlibrary/additems(_:))*