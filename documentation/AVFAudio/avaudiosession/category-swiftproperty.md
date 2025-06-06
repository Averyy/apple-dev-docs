# category

**Framework**: AVFAudio  
**Kind**: property

The current audio session category.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var category: AVAudioSession.Category { get }
```

#### Discussion

An audio session category defines a set of audio behaviors for your app. The default category assigned to an audio session is [`soloAmbient`](avaudiosession/category-swift.struct/soloambient.md).

## See Also

- [var availableCategories: [AVAudioSession.Category]](avaudiosession/availablecategories.md)
  The audio session categories available on the current device.
- [AVAudioSession.Category](avaudiosession/category-swift.struct.md)
  Audio session category identifiers.
- [var categoryOptions: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.property.md)
  The set of options associated with the current audio session category.
- [AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct.md)
  Constants that specify optional audio behaviors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/category-swift.property)*