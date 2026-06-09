# categoryOptions

**Framework**: AVFAudio  
**Kind**: property

The set of options associated with the current audio session category.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var categoryOptions: AVAudioSession.CategoryOptions { get }
```

#### Discussion

You use category options to tailor the behavior of the active audio session category. See [`AVAudioSession.CategoryOptions`](avaudiosession/categoryoptions-swift.struct.md) for the supported values.

## See Also

- [var category: AVAudioSession.Category](avaudiosession/category-swift.property.md)
  The current audio session category.
- [var availableCategories: [AVAudioSession.Category]](avaudiosession/availablecategories.md)
  The audio session categories available on the current device.
- [AVAudioSession.Category](avaudiosession/category-swift.struct.md)
  Audio session category identifiers.
- [AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct.md)
  Constants that specify optional audio behaviors.
- [static var farFieldInput: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/farfieldinput.md)
  This option should be used if a session prefers to use FarFieldInput when available. This option is only valid with categories that support input - [`playAndRecord`](avaudiosession/category-swift.struct/playandrecord.md), [`record`](avaudiosession/category-swift.struct/record.md), and `AVAudioSessionMultiRoute` with [`dualRoute`](avaudiosession/mode-swift.struct/dualroute.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/categoryoptions-swift.property)*