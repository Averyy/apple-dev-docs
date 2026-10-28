# category

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) AVAudioSessionCategory category;
```

## Discussion

An audio session category defines a set of audio behaviors for your app. The default category assigned to an audio session is [`soloAmbient`](./category-swift.struct/soloambient.md).

## See Also

### Inspecting the category configuration
- [var availableCategories: [AVAudioSession.Category]](./availablecategories.md)
  The audio session categories available on the current device.
- [AVAudioSession.Category](./category-swift.struct.md)
  Audio session category identifiers.
- [var categoryOptions: AVAudioSession.CategoryOptions](./categoryoptions-swift.property.md)
  The set of options associated with the current audio session category.
- [AVAudioSession.CategoryOptions](./categoryoptions-swift.struct.md)
  Constants that specify optional audio behaviors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/category-swift.property)*