# playableMediaSelectionOptions(from:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns an array containing the media selection options from a given array that are playable.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
class func playableMediaSelectionOptions(from mediaSelectionOptions: [AVMediaSelectionOption]) -> [AVMediaSelectionOption]
```

```objc
+ (NSArray<AVMediaSelectionOption *> *) playableMediaSelectionOptionsFromArray:(NSArray<AVMediaSelectionOption *> *) mediaSelectionOptions;
```

## Return Value

An array containing the media selection options from `array` that are playable.

## Parameters

- `mediaSelectionOptions`: An array of [`AVMediaSelectionOption`](../avmediaselectionoption.md) objects to be filtered by playability.

## See Also

### Filtering selection options
- [class func mediaSelectionOptions(from: [AVMediaSelectionOption], with: Locale) -> [AVMediaSelectionOption]](./mediaselectionoptions%28from,with%29.md)
  Returns an array containing the media selection options from a given array that match the specified locale.
- [class func mediaSelectionOptions(from: [AVMediaSelectionOption], withMediaCharacteristics: [AVMediaCharacteristic]) -> [AVMediaSelectionOption]](./mediaselectionoptions%28from,withmediacharacteristics%29.md)
  Returns an array containing the media selection options from a given array that match given media characteristics.
- [class func mediaSelectionOptions(from: [AVMediaSelectionOption], withoutMediaCharacteristics: [AVMediaCharacteristic]) -> [AVMediaSelectionOption]](./mediaselectionoptions%28from,withoutmediacharacteristics%29.md)
  Returns an array containing the media selection options from a given array that do not match given media characteristics.
- [class func mediaSelectionOptions(from: [AVMediaSelectionOption], filteredAndSortedAccordingToPreferredLanguages: [String]) -> [AVMediaSelectionOption]](./mediaselectionoptions%28from,filteredandsortedaccordingtopreferredlanguages%29.md)
  Returns an array of media selection options, filtering them according to whether their locales match one of the specified languages.
- [var customMediaSelectionScheme: AVCustomMediaSelectionScheme?](./custommediaselectionscheme.md)
  For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVCustomMediaSelectionScheme provides a collection of custom settings for controlling the presentation of the media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/playablemediaselectionoptions(from:))*