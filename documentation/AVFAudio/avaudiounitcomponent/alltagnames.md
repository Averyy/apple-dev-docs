# allTagNames

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

An array of tag names for the audio unit component.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var allTagNames: [String] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSString *> * allTagNames;
```

## See Also

### Getting Audio Unit component tags
- [var iconURL: URL?](./iconurl.md)
  The URL of an icon that represents the audio unit component.
- [var icon: UIImage?](./icon.md)
  An icon that represents the component.
- [var localizedTypeName: String](./localizedtypename.md)
  The localized type name of the component.
- [var userTagNames: [String]](./usertagnames.md)
  An array of tags the user creates.
- [AVAudioUnitComponent.TagsDidChangeMessage](./tagsdidchangemessage.md)
  Type-safe notification message for audio unit component tag changes.
- [AVAudioUnitComponentTagsDidChangeNotification](../avaudiounitcomponenttagsdidchangenotification.md)
  A notification that indicates when component tags change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitcomponent/alltagnames)*