# mediaSelectionOptions(from:with:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns an array containing the media selection options from a given array that match the specified locale.

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
class func mediaSelectionOptions(from mediaSelectionOptions: [AVMediaSelectionOption], with locale: Locale) -> [AVMediaSelectionOption]
```

```objc
+ (NSArray<AVMediaSelectionOption *> *) mediaSelectionOptionsFromArray:(NSArray<AVMediaSelectionOption *> *) mediaSelectionOptions withLocale:(NSLocale *) locale;
```

#### Return Value

An array containing the media selection options from `array` that match the `locale`.

## Parameters

- `mediaSelectionOptions`: An array of [`AVMediaSelectionOption`](../avmediaselectionoption.md) objects to be filtered.
- `locale`: The locale that must be matched for a media selection option to be copied to the output array.

## See Also

### Filtering selection options
- [class func playableMediaSelectionOptions(from: [AVMediaSelectionOption]) -> [AVMediaSelectionOption]](./playablemediaselectionoptions%28from%29.md)
  Returns an array containing the media selection options from a given array that are playable.
- [class func mediaSelectionOptions(from: [AVMediaSelectionOption], withMediaCharacteristics: [AVMediaCharacteristic]) -> [AVMediaSelectionOption]](./mediaselectionoptions%28from,withmediacharacteristics%29.md)
  Returns an array containing the media selection options from a given array that match given media characteristics.
- [class func mediaSelectionOptions(from: [AVMediaSelectionOption], withoutMediaCharacteristics: [AVMediaCharacteristic]) -> [AVMediaSelectionOption]](./mediaselectionoptions%28from,withoutmediacharacteristics%29.md)
  Returns an array containing the media selection options from a given array that do not match given media characteristics.
- [class func mediaSelectionOptions(from: [AVMediaSelectionOption], filteredAndSortedAccordingToPreferredLanguages: [String]) -> [AVMediaSelectionOption]](./mediaselectionoptions%28from,filteredandsortedaccordingtopreferredlanguages%29.md)
  Returns an array of media selection options, filtering them according to whether their locales match one of the specified languages.
- [var customMediaSelectionScheme: AVCustomMediaSelectionScheme?](./custommediaselectionscheme.md)
  For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVCustomMediaSelectionScheme provides a collection of custom settings for controlling the presentation of the media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/mediaselectionoptions(from:with:))*