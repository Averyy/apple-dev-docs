# mediaCharacteristics

**Framework**: AVKit  
**Kind**: property

The media characteristics describing accessibility features and content properties of this option. Common values include `AVMediaCharacteristicContainsOnlyForcedSubtitles`, `AVMediaCharacteristicTranscribesSpokenDialogForAccessibility`, and `AVMediaCharacteristicDescribesMusicAndSoundForAccessibility`. May be empty if no characteristics apply.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
var mediaCharacteristics: [AVMediaCharacteristic] { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacemediaselectionoption/mediacharacteristics)*