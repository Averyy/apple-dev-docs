# SHLibrary

**Framework**: ShazamKit  
**Kind**: class  
**Role**: Class

An object that represents a user’s synced Shazam library.

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
final class SHLibrary
```

## Topics

### Managing the items in the library
- [static let `default`: SHLibrary](./shlibrary/default.md)
  An instance of the default Shazam library.
- [func addItems([SHMediaItem]) async throws](./shlibrary/additems%28_%29.md)
  Adds an array of media items to the user’s Shazam library.
- [func removeItems([SHMediaItem]) async throws](./shlibrary/removeitems%28_%29.md)
  Removes an array of media items from the user’s Shazam library.
- [var items: [SHMediaItem]](./shlibrary/items.md)
  The list of synced items in the Media Library.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Escapable](../Swift/escapable.md)
- [Observable](../Observation/observable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Update the user’s Shazam library
- [class SHMediaLibrary](./shmedialibrary.md)
  An object that represents the user’s Shazam library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shlibrary)*