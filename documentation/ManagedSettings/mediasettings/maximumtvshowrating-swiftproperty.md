# maximumTVShowRating

**Framework**: ManagedSettings  
**Kind**: property

The maximum TV show rating that the user may view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var maximumTVShowRating: Int? { get set }
```

#### Discussion

If your app doesn’t configure this setting, the value is `nil`. The following list provides U.S. descriptions for the ratings:

- `1000`: All
- `600`: TM-MA
- `500`: TV-14
- `400`: TV-PG
- `300`: TV-G
- `200`: TV-Y7
- `100`: TV-Y
- `0`: None

## See Also

- [var maximumMovieRating: Int?](mediasettings/maximummovierating-swift.property.md)
  The maximum movie rating the user may view.
- [static let maximumMovieRating: BoundedSettingMetadata<Int>](mediasettings/maximummovierating-swift.type.property.md)
  The metadata for the setting that controls the maximum movie rating.
- [static let maximumTVShowRating: BoundedSettingMetadata<Int>](mediasettings/maximumtvshowrating-swift.type.property.md)
  The metadata for the setting that controls the maximum TV show rating.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/mediasettings/maximumtvshowrating-swift.property)*