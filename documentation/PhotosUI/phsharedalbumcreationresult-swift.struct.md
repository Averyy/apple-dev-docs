# PHSharedAlbumCreationResult

**Framework**: PhotosUI  
**Kind**: struct  
**Role**: Structure

The result of a user creating a shared album.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct PHSharedAlbumCreationResult
```

## Topics

### Instance Properties
- [var albumIdentifier: String?](./phsharedalbumcreationresult-swift.struct/albumidentifier.md)
  The identifier of the created shared album. `nil` if creation failed.
- [var albumURL: URL?](./phsharedalbumcreationresult-swift.struct/albumurl.md)
  The URL of the created shared album. `nil` if creation failed.
- [var error: (any Error)?](./phsharedalbumcreationresult-swift.struct/error.md)
  An error describing why shared album creation failed, if it failed. `nil` on success.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phsharedalbumcreationresult-swift.struct)*