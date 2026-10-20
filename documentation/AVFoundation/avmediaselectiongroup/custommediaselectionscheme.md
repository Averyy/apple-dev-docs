# customMediaSelectionScheme

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVCustomMediaSelectionScheme provides a collection of custom settings for controlling the presentation of the media.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var customMediaSelectionScheme: AVCustomMediaSelectionScheme? { get }
```

```objc
@property (nonatomic, readonly, nullable) AVCustomMediaSelectionScheme * customMediaSelectionScheme;
```

## See Also

### Filtering selection options
- [class func playableMediaSelectionOptions(from: [AVMediaSelectionOption]) -> [AVMediaSelectionOption]](./playablemediaselectionoptions%28from%29.md)
  Returns an array containing the media selection options from a given array that are playable.
- [class func mediaSelectionOptions(from: [AVMediaSelectionOption], with: Locale) -> [AVMediaSelectionOption]](./mediaselectionoptions%28from,with%29.md)
  Returns an array containing the media selection options from a given array that match the specified locale.
- [class func mediaSelectionOptions(from: [AVMediaSelectionOption], withMediaCharacteristics: [AVMediaCharacteristic]) -> [AVMediaSelectionOption]](./mediaselectionoptions%28from,withmediacharacteristics%29.md)
  Returns an array containing the media selection options from a given array that match given media characteristics.
- [class func mediaSelectionOptions(from: [AVMediaSelectionOption], withoutMediaCharacteristics: [AVMediaCharacteristic]) -> [AVMediaSelectionOption]](./mediaselectionoptions%28from,withoutmediacharacteristics%29.md)
  Returns an array containing the media selection options from a given array that do not match given media characteristics.
- [class func mediaSelectionOptions(from: [AVMediaSelectionOption], filteredAndSortedAccordingToPreferredLanguages: [String]) -> [AVMediaSelectionOption]](./mediaselectionoptions%28from,filteredandsortedaccordingtopreferredlanguages%29.md)
  Returns an array of media selection options, filtering them according to whether their locales match one of the specified languages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/custommediaselectionscheme)*