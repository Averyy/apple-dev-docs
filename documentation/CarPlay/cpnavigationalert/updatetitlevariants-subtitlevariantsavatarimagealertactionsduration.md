# updateTitleVariants(_:subtitleVariants:avatarImage:alert:actions:duration:)

**Framework**: CarPlay  
**Kind**: method

Update the navigation alert with new title variants, subtitle variants, image, actions, and duration.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
func updateTitleVariants(_ newTitleVariants: [String], subtitleVariants newSubtitleVariants: [String], avatarImage: UIImage?, alert alertImage: UIImage?, actions: [CPAlertAction], duration: TimeInterval)
```

#### Discussion

Updating an alert that has already been dismissed has no effect.

When providing an image, your app should provide a @c UIImage that is display-ready. If necessary for the image, provide light and dark styles by using an asset from your asset catalog, prepared with light and dark styles or by using @c UIImageAsset to combine two @c UIImage instances into a single image with both styles.

UIImageAsset is used to combine multiple UIImages with different trait collections into a single UIImage.

## Parameters

- `newTitleVariants`: An updated array of title variants.
- `newSubtitleVariants`: An updated array of subtitle variants.
- `avatarImage`: An optional updated @c UIImage to display.
- `alertImage`: An optional updated @c UIImage to display. Note that this image may be hidden by the system if the available screen space is too small.
- `actions`: An updated array of @c CPAlertAction objects. The number of actions will be clamped to @c maximumActionsCount.
- `duration`: The updated duration for which this alert should be visible. Specify -1 to keep duration unaltered. Specify 0 for an alert that displays indefinitely.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationalert/updatetitlevariants(_:subtitlevariants:avatarimage:alert:actions:duration:))*