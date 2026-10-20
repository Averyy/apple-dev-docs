# availableMediaCharacteristicsWithMediaSelectionOptions

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An array of media characteristics for which a media selection option is available.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var availableMediaCharacteristicsWithMediaSelectionOptions: [AVMediaCharacteristic] { get }
```

## See Also

### Accessing media selections
- [var allMediaSelections: [AVMediaSelection]](./allmediaselections.md)
  The array of available media selections for this asset.
- [func mediaSelectionGroup(forMediaCharacteristic: AVMediaCharacteristic) -> AVMediaSelectionGroup?](./mediaselectiongroup%28formediacharacteristic%29.md)
  Returns a media selection group that contains one or more options with the specified media characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/availablemediacharacteristicswithmediaselectionoptions)*