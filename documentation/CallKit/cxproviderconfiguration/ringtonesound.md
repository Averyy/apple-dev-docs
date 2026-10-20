# ringtoneSound

**Framework**: CallKit  
**Kind**: property  
**Role**: Instance Property

The name of the sound resource in the app bundle to be used for the provider ringtone.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var ringtoneSound: String? { get set }
```

```objc
@property (nonatomic, strong, nullable) NSString * ringtoneSound;
```

## See Also

### Configuring Native Call UI
- [var localizedName: String?](./localizedname.md)
  The localized name of the provider.
- [var iconTemplateImageData: Data?](./icontemplateimagedata.md)
  The PNG data for the icon image to be displayed for the provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxproviderconfiguration/ringtonesound)*