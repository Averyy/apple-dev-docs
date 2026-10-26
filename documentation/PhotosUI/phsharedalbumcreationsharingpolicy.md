# PHSharedAlbumCreationSharingPolicy

**Framework**: PhotosUI  
**Kind**: enum  
**Role**: Enumeration

The sharing policy for creating shared albums.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum PHSharedAlbumCreationSharingPolicy
```

```c
enum PHSharedAlbumCreationSharingPolicy : NSInteger;
```

## Topics

### Enumeration Cases
- [PHSharedAlbumCreationSharingPolicy.private](./phsharedalbumcreationsharingpolicy/private.md)
  The policy for requiring that only people the user approves or invites are allowed to access the shared album.
- [PHSharedAlbumCreationSharingPolicy.public](./phsharedalbumcreationsharingpolicy/public.md)
  The policy for allowing anyone, without approval, to access the shared album.
### Initializers
- [init?(rawValue: Int)](./phsharedalbumcreationsharingpolicy/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phsharedalbumcreationsharingpolicy)*