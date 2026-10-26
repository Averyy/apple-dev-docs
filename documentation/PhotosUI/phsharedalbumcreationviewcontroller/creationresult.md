# creationResult

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

Upon successful album creation, `creationResult` will be non-nil and provide information about the just-created shared album.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@NSCopying
var creationResult: __PHSharedAlbumCreationResult? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) PHSharedAlbumCreationResult * creationResult;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phsharedalbumcreationviewcontroller/creationresult)*