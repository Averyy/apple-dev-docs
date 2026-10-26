# PHSharedAlbumCreationConfiguration

**Framework**: PhotosUI  
**Kind**: struct  
**Role**: Structure

An object used to configure a `PHSharedAlbumCreationViewController`.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct PHSharedAlbumCreationConfiguration
```

## Topics

### Initializers
- [init(photoLibrary: PHPhotoLibrary)](./phsharedalbumcreationconfiguration-swift.struct/init%28photolibrary%29.md)
### Instance Properties
- [var defaultPolicy: PHSharedAlbumCreationSharingPolicy](./phsharedalbumcreationconfiguration-swift.struct/defaultpolicy.md)
  The default sharing policy of the shared album. If not specified, this defaults to `PHSharedAlbumCreationSharingPolicyPrivate`.
- [var defaultTitle: String?](./phsharedalbumcreationconfiguration-swift.struct/defaulttitle.md)
  The default title for the shared album. Useful for suggesting a relevant title to the user. Defaults to `nil`.
- [let photoLibrary: PHPhotoLibrary](./phsharedalbumcreationconfiguration-swift.struct/photolibrary.md)
  The photo library in which the shared album will be created.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phsharedalbumcreationconfiguration-swift.struct)*