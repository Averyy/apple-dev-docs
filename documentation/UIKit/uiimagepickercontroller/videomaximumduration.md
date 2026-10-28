# videoMaximumDuration

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The maximum duration, in seconds, for a video recording.

**Availability**:
- iOS 3.1+
- iPadOS 3.1+
- Mac Catalyst 13.1+

## Declaration

```swift
var videoMaximumDuration: TimeInterval { get set }
```

```objc
@property (nonatomic) NSTimeInterval videoMaximumDuration;
```

## Discussion

The default value for this property is 10 minutes (600 seconds). When a user taps the Share button to send a movie to MMS, MobileMe, YouTube, or another destination, an appropriate duration limit and an appropriate video quality are enforced.

This property is available only if the [`mediaTypes`](./mediatypes.md) property’s value array includes the `kUTTypeMovie` media type.

## See Also

### Related Documentation
- [class func availableMediaTypes(for: UIImagePickerController.SourceType) -> [String]?](./availablemediatypes%28for%29.md)
  Retrieves the available media types for the specified source type.
- [class func isSourceTypeAvailable(UIImagePickerController.SourceType) -> Bool](./issourcetypeavailable%28_%29.md)
  Queries whether the device supports picking media using the specified source type.
### Configuring the video capture options
- [var videoQuality: UIImagePickerController.QualityType](./videoquality.md)
  The video recording and transcoding quality.
- [UIImagePickerController.QualityType](./qualitytype.md)
  Constants that describe video quality settings for movies that are recorded with the built-in camera, or that are transcoded when they’re displayed in the image picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/videomaximumduration)*