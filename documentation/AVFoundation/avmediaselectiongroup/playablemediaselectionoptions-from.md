# playableMediaSelectionOptions(from:)

**Framework**: AVFoundation  
**Kind**: method

Returns an array containing the media selection options from a given array that are playable.

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
class func playableMediaSelectionOptions(from mediaSelectionOptions: [AVMediaSelectionOption]) -> [AVMediaSelectionOption]
```

#### Return Value

An array containing the media selection options from `array` that are playable.

## Parameters

- `mediaSelectionOptions`: An array of   objects to be filtered by playability.

## See Also

- [class func mediaSelectionOptions(from: [AVMediaSelectionOption], with: Locale) -> [AVMediaSelectionOption]](avmediaselectiongroup/mediaselectionoptions(from:with:).md)
  Returns an array containing the media selection options from a given array that match the specified locale.
- [class func mediaSelectionOptions(from: [AVMediaSelectionOption], withMediaCharacteristics: [AVMediaCharacteristic]) -> [AVMediaSelectionOption]](avmediaselectiongroup/mediaselectionoptions(from:withmediacharacteristics:).md)
  Returns an array containing the media selection options from a given array that match given media characteristics.
- [class func mediaSelectionOptions(from: [AVMediaSelectionOption], withoutMediaCharacteristics: [AVMediaCharacteristic]) -> [AVMediaSelectionOption]](avmediaselectiongroup/mediaselectionoptions(from:withoutmediacharacteristics:).md)
  Returns an array containing the media selection options from a given array that do not match given media characteristics.
- [class func mediaSelectionOptions(from: [AVMediaSelectionOption], filteredAndSortedAccordingToPreferredLanguages: [String]) -> [AVMediaSelectionOption]](avmediaselectiongroup/mediaselectionoptions(from:filteredandsortedaccordingtopreferredlanguages:).md)
  Returns an array of media selection options, filtering them according to whether their locales match one of the specified languages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/playablemediaselectionoptions(from:))*