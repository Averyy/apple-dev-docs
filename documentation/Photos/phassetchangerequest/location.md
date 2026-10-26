# location

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The location information saved with the asset.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var location: CLLocation? { get set }
```

```objc
@property (nonatomic, strong, readwrite, nullable) CLLocation * location;
```

#### Discussion

Typically, an asset’s location metadata identifies the place where the asset was captured. Use this property to provide a different location.

## See Also

### Modifying Assets
- [convenience init(for: PHAsset)](./init%28for%29.md)
  Creates a request for modifying the specified asset.
- [var creationDate: Date?](./creationdate.md)
  The date and time at which the asset claims to have been originally created.
- [var isFavorite: Bool](./isfavorite.md)
  A Boolean value that indicates whether the asset is marked as one of the user’s favorites.
- [var isHidden: Bool](./ishidden.md)
  A Boolean value that indicates whether the asset is hidden in collections.
- [var caption: String?](./caption.md)
  An asset description to change to. Set to nil or an empty string to clear the caption.
- [func addKeyword(String)](./addkeyword%28_%29.md)
  Add or remove a keyword associated with this asset Adding a keyword that is already associated (or removing a keyword that is not) will be silently ignored
- [func removeKeyword(String)](./removekeyword%28_%29.md)
- [var rating: PHAsset.Rating](./rating.md)
  The rating for this asset
- [func setLivePhotoVideoPlaybackEnabled(Bool)](./setlivephotovideoplaybackenabled%28_%29.md)
  Disable or enable the video part of a Live Photo so it just appears as a still image (disabled) or a Live Photo (enabled)


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetchangerequest/location)*