# items

**Framework**: ShazamKit  
**Kind**: property

The list of synced items in the Media Library.

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
@MainActor
final var items: [SHMediaItem] { get }
```

## See Also

- [static let `default`: SHLibrary](shlibrary/default.md)
  An instance of the default Shazam library.
- [func addItems([SHMediaItem]) async throws](shlibrary/additems(_:).md)
  Adds an array of media items to the user’s Shazam library.
- [func removeItems([SHMediaItem]) async throws](shlibrary/removeitems(_:).md)
  Removes an array of media items from the user’s Shazam library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shlibrary/items)*