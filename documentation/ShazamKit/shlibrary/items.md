# items

**Framework**: ShazamKit  
**Kind**: property  
**Role**: Instance Property

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

### Managing the items in the library
- [static let `default`: SHLibrary](./default.md)
  An instance of the default Shazam library.
- [func addItems([SHMediaItem]) async throws](./additems%28_%29.md)
  Adds an array of media items to the user’s Shazam library.
- [func removeItems([SHMediaItem]) async throws](./removeitems%28_%29.md)
  Removes an array of media items from the user’s Shazam library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shlibrary/items)*