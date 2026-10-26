# availableMediaCharacteristicsWithMediaSelectionOptions

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An array of media characteristics for which a media selection option is available.

**Availability**:
- iOS 5.0+ - Deprecated in 16.0
- iPadOS 5.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.8+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`availableMediaCharacteristicsWithMediaSelectionOptions`](../avpartialasyncproperty/availablemediacharacteristicswithmediaselectionoptions.md) asynchronously instead.

## Declaration

```swift
var availableMediaCharacteristicsWithMediaSelectionOptions: [AVMediaCharacteristic] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSString *> * availableMediaCharacteristicsWithMediaSelectionOptions;
```

## Mentions

- [Selecting subtitles and alternative audio tracks](../selecting-subtitles-and-alternative-audio-tracks.md)

## See Also

### Accessing media selections
- [allMediaSelections](./allmediaselections.md)
  The array of available media selections for this asset.
- [- mediaSelectionGroupForMediaCharacteristic:](./mediaselectiongroup%28formediacharacteristic%29.md)
  Returns a media selection group that contains one or more options with the specified media characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/availablemediacharacteristicswithmediaselectionoptions)*