# AVAudioUnitComponentTagsDidChangeNotification

**Framework**: AVFAudio  
**Kind**: var  
**Role**: Global Variable

A notification that indicates when component tags change.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```c
extern NSString * const AVAudioUnitComponentTagsDidChangeNotification;
```

#### Discussion

The notification object contains the `AVAudioUnitComponent` object with the tags.

## See Also

### Getting Audio Unit component tags
- [var iconURL: URL?](./avaudiounitcomponent/iconurl.md)
  The URL of an icon that represents the audio unit component.
- [var icon: UIImage?](./avaudiounitcomponent/icon.md)
  An icon that represents the component.
- [var localizedTypeName: String](./avaudiounitcomponent/localizedtypename.md)
  The localized type name of the component.
- [var allTagNames: [String]](./avaudiounitcomponent/alltagnames.md)
  An array of tag names for the audio unit component.
- [var userTagNames: [String]](./avaudiounitcomponent/usertagnames.md)
  An array of tags the user creates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitcomponenttagsdidchangenotification)*