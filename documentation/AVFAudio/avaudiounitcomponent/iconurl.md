# iconURL

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The URL of an icon that represents the audio unit component.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var iconURL: URL? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSURL * iconURL;
```

## See Also

### Getting Audio Unit component tags
- [var icon: UIImage?](./icon.md)
  An icon that represents the component.
- [var localizedTypeName: String](./localizedtypename.md)
  The localized type name of the component.
- [var allTagNames: [String]](./alltagnames.md)
  An array of tag names for the audio unit component.
- [var userTagNames: [String]](./usertagnames.md)
  An array of tags the user creates.
- [AVAudioUnitComponent.TagsDidChangeMessage](./tagsdidchangemessage.md)
  Type-safe notification message for audio unit component tag changes.
- [AVAudioUnitComponentTagsDidChangeNotification](../avaudiounitcomponenttagsdidchangenotification.md)
  A notification that indicates when component tags change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitcomponent/iconurl)*