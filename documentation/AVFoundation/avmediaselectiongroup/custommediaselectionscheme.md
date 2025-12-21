# customMediaSelectionScheme

**Framework**: AVFoundation  
**Kind**: property

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

## See Also

- [class func playableMediaSelectionOptions(from: [AVMediaSelectionOption]) -> [AVMediaSelectionOption]](avmediaselectiongroup/playablemediaselectionoptions(from:).md)
  Returns an array containing the media selection options from a given array that are playable.
- [class func mediaSelectionOptions(from: [AVMediaSelectionOption], with: Locale) -> [AVMediaSelectionOption]](avmediaselectiongroup/mediaselectionoptions(from:with:).md)
  Returns an array containing the media selection options from a given array that match the specified locale.
- [class func mediaSelectionOptions(from: [AVMediaSelectionOption], withMediaCharacteristics: [AVMediaCharacteristic]) -> [AVMediaSelectionOption]](avmediaselectiongroup/mediaselectionoptions(from:withmediacharacteristics:).md)
  Returns an array containing the media selection options from a given array that match given media characteristics.
- [class func mediaSelectionOptions(from: [AVMediaSelectionOption], withoutMediaCharacteristics: [AVMediaCharacteristic]) -> [AVMediaSelectionOption]](avmediaselectiongroup/mediaselectionoptions(from:withoutmediacharacteristics:).md)
  Returns an array containing the media selection options from a given array that do not match given media characteristics.
- [class func mediaSelectionOptions(from: [AVMediaSelectionOption], filteredAndSortedAccordingToPreferredLanguages: [String]) -> [AVMediaSelectionOption]](avmediaselectiongroup/mediaselectionoptions(from:filteredandsortedaccordingtopreferredlanguages:).md)
  Returns an array of media selection options, filtering them according to whether their locales match one of the specified languages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/custommediaselectionscheme)*