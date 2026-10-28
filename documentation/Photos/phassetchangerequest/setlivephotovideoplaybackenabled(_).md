# setLivePhotoVideoPlaybackEnabled(_:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Disable or enable the video part of a Live Photo so it just appears as a still image (disabled) or a Live Photo (enabled)

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func setLivePhotoVideoPlaybackEnabled(_ enabled: Bool)
```

```objc
- (void) setLivePhotoVideoPlaybackEnabled:(BOOL) enabled;
```

## Discussion

Applies to Live Photos only.

## See Also

### Modifying Assets
- [convenience init(for: PHAsset)](./init%28for%29.md)
  Creates a request for modifying the specified asset.
- [var creationDate: Date?](./creationdate.md)
  The date and time at which the asset claims to have been originally created.
- [var location: CLLocation?](./location.md)
  The location information saved with the asset.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetchangerequest/setlivephotovideoplaybackenabled(_:))*