# authorDisplayName

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

App defined display name for the playlist.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var authorDisplayName: String! { get set }
```

```objc
@property (nonatomic, copy, null_resettable) NSString * authorDisplayName;
```

## Discussion

The system requires this property for 3rd party apps. Defaults to the app display name when not defined.

## See Also

### Metadata for a playlist
- [var descriptionText: String](./descriptiontext.md)
  The descriptive text for the playlist.
- [var name: String](./name.md)
  The playlist’s displayed name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylistcreationmetadata/authordisplayname)*