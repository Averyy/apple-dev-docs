# mediaSelectionOptions(from:withoutMediaCharacteristics:)

**Framework**: AVFoundation  
**Kind**: method

Returns an array containing the media selection options from a given array that do not match given media characteristics.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class func mediaSelectionOptions(from mediaSelectionOptions: [AVMediaSelectionOption], withoutMediaCharacteristics mediaCharacteristics: [AVMediaCharacteristic]) -> [AVMediaSelectionOption]
```

#### Return Value

An array containing the media selection options from `array` that lack the media characteristics in `mediaCharacteristics`.

## Parameters

- `mediaSelectionOptions`: An array of   objects to be filtered.
- `mediaCharacteristics`: The media characteristics that must not be present for a media selection option to be present in the output array.

## See Also

- [class func playableMediaSelectionOptions(from: [AVMediaSelectionOption]) -> [AVMediaSelectionOption]](avmediaselectiongroup/playablemediaselectionoptions(from:).md)
  Returns an array containing the media selection options from a given array that are playable.
- [class func mediaSelectionOptions(from: [AVMediaSelectionOption], with: Locale) -> [AVMediaSelectionOption]](avmediaselectiongroup/mediaselectionoptions(from:with:).md)
  Returns an array containing the media selection options from a given array that match the specified locale.
- [class func mediaSelectionOptions(from: [AVMediaSelectionOption], withMediaCharacteristics: [AVMediaCharacteristic]) -> [AVMediaSelectionOption]](avmediaselectiongroup/mediaselectionoptions(from:withmediacharacteristics:).md)
  Returns an array containing the media selection options from a given array that match given media characteristics.
- [class func mediaSelectionOptions(from: [AVMediaSelectionOption], filteredAndSortedAccordingToPreferredLanguages: [String]) -> [AVMediaSelectionOption]](avmediaselectiongroup/mediaselectionoptions(from:filteredandsortedaccordingtopreferredlanguages:).md)
  Returns an array of media selection options, filtering them according to whether their locales match one of the specified languages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/mediaselectionoptions(from:withoutmediacharacteristics:))*