# removeItems(_:)

**Framework**: ShazamKit  
**Kind**: method

Removes an array of media items from the user’s Shazam library.

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
final func removeItems(_ items: [SHMediaItem]) async throws
```

#### Discussion

Apps can only remove media items that it added to the library with [`addItems(_:)`](shlibrary/additems(_:).md).

This throws [`SHError.Code.mediaLibrarySyncFailed`](sherror/code/medialibrarysyncfailed.md) if the system can’t remove at least one [`SHMediaItem`](shmediaitem.md) or if an error occurred during the removal. In that case, the system doesn’t remove any items from the library.

## Parameters

- `items`: An array containing the   objects to remove from the library.

## See Also

- [static let `default`: SHLibrary](shlibrary/default.md)
  An instance of the default Shazam library.
- [func addItems([SHMediaItem]) async throws](shlibrary/additems(_:).md)
  Adds an array of media items to the user’s Shazam library.
- [var items: [SHMediaItem]](shlibrary/items.md)
  The list of synced items in the Media Library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shlibrary/removeitems(_:))*