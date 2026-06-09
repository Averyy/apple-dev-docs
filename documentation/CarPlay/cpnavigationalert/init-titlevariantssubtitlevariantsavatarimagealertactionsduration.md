# init(titleVariants:subtitleVariants:avatarImage:alert:actions:duration:)

**Framework**: CarPlay  
**Kind**: init

Initialize a @c CPNavigationAlert with a title, image, an array of actions, and duration.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
init(titleVariants: [String], subtitleVariants: [String], avatarImage: UIImage?, alert alertImage: UIImage?, actions: [CPAlertAction], duration: TimeInterval)
```

#### Return Value

An initialized @c CPNavigationAlert.

## Parameters

- `titleVariants`: An array of titles. The system will select a title that fits in the available space. The variant strings should be provided as localized, displayable content.
- `subtitleVariants`: An array of subtitles. The system will select a subtitle that fits in the available space. The variant strings should be provided as localized, displayable content.
- `avatarImage`: An optional @c UIImage to display in this navigation alert. Animated images are not supported. It will be displayed in the top leading corner.
- `alertImage`: An optional @c UIImage to display in this navigation alert. Animated images are not supported. It will be displayed above the action buttons. Note that this image may be hidden by the system if the available screen space is too small.
- `actions`: An array of @c CPAlertAction objects. The number of actions will be clamped to @c maximumActionsCount.
- `duration`: The duration for which this alert should be visible. Specify 0 for an alert that displays indefinitely.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationalert/init(titlevariants:subtitlevariants:avatarimage:alert:actions:duration:))*