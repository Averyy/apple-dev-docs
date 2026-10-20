# maximumTVShowRating

**Framework**: Managed Settings  
**Kind**: property  
**Role**: Type Property

The metadata for the setting that controls the maximum TV show rating.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
static let maximumTVShowRating: BoundedSettingMetadata<Int>
```

#### Discussion

The default value is `1000` and the bounds are `0...1000`.

## See Also

### Limiting movie and TV show ratings
- [var maximumMovieRating: Int?](./maximummovierating-swift.property.md)
  The maximum movie rating the user may view.
- [var maximumTVShowRating: Int?](./maximumtvshowrating-swift.property.md)
  The maximum TV show rating that the user may view.
- [static let maximumMovieRating: BoundedSettingMetadata<Int>](./maximummovierating-swift.type.property.md)
  The metadata for the setting that controls the maximum movie rating.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/mediasettings/maximumtvshowrating-swift.type.property)*