# maximumMovieRating

**Framework**: Managed Settings  
**Kind**: property

The maximum movie rating the user may view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+

## Declaration

```swift
var maximumMovieRating: Int? { get set }
```

## Mentions

- [Confirming the effective TV and movie ratings](readingmedia.md)

#### Discussion

If your app doesn’t configure this setting, the value is `nil`. The following list provides U.S. descriptions for the ratings:

- `1000`: All
- `500`: NC-17
- `400`: R
- `300`: PG-13
- `200`: PG
- `100`: G
- `0`: None

## See Also

- [var maximumTVShowRating: Int?](mediasettings/maximumtvshowrating-swift.property.md)
  The maximum TV show rating that the user may view.
- [static let maximumMovieRating: BoundedSettingMetadata<Int>](mediasettings/maximummovierating-swift.type.property.md)
  The metadata for the setting that controls the maximum movie rating.
- [static let maximumTVShowRating: BoundedSettingMetadata<Int>](mediasettings/maximumtvshowrating-swift.type.property.md)
  The metadata for the setting that controls the maximum TV show rating.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/mediasettings/maximummovierating-swift.property)*