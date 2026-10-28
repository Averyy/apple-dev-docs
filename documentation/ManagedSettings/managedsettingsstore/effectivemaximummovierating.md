# effectiveMaximumMovieRating

**Framework**: Managed Settings  
**Kind**: property  
**Role**: Instance Property

The movie rating constraint that is active on this device.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 26.0+

## Declaration

```swift
@Published
<Int> var effectiveMaximumMovieRating: Int { get }
```

## Mentions

- [Confirming the effective TV and movie ratings](../readingmedia.md)

## Discussion

An authorized app can use the Family Controls framework to apply a [`maximumMovieRating`](../mediasettings/maximummovierating-swift.property.md) to the device. If no `maximumMovieRating` settings are active, then the value of this property is the default value of [`maximumMovieRating`](../mediasettings/maximummovierating-swift.type.property.md). The system publishes changes dynamically.

## See Also

### Filtering media content
- [var appStore: AppStoreSettings](./appstore.md)
  Settings that affect the App Store.
- [struct AppStoreSettings](../appstoresettings.md)
  Constraints on a user’s App Store settings.
- [var application: ApplicationSettings](./application.md)
  Settings that affect applications.
- [struct ApplicationSettings](../applicationsettings.md)
  Constraints on the apps and categories of apps a user can run on their device.
- [var effectiveMaximumTVShowRating: Int](./effectivemaximumtvshowrating.md)
  The TV rating constraint that is active on this device.
- [var gameCenter: GameCenterSettings](./gamecenter.md)
  Settings that affect Game Center.
- [struct GameCenterSettings](../gamecentersettings.md)
  Constraints on the user’s Game Center settings.
- [var media: MediaSettings](./media.md)
  Settings that affect media.
- [struct MediaSettings](../mediasettings.md)
  Constraints on the media content the user can access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/managedsettingsstore/effectivemaximummovierating)*