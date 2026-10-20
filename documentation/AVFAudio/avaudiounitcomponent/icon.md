# icon

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

An icon that represents the component.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 10.11+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
var icon: UIImage? { get }
```

*macOS*

```swift
var icon: NSImage? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly, nullable) UIImage * icon;
```

*macOS*

```objc
@property (nonatomic, readonly, nullable) NSImage * icon;
```

## See Also

### Getting Audio Unit component tags
- [var iconURL: URL?](./iconurl.md)
  The URL of an icon that represents the audio unit component.
- [var localizedTypeName: String](./localizedtypename.md)
  The localized type name of the component.
- [var allTagNames: [String]](./alltagnames.md)
  An array of tag names for the audio unit component.
- [var userTagNames: [String]](./usertagnames.md)
  An array of tags the user creates.
- [AVAudioUnitComponent.TagsDidChangeMessage](./tagsdidchangemessage.md)
  Type-safe notification message for audio unit component tag changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitcomponent/icon)*