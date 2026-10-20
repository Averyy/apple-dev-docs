# categoryOptions

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) AVAudioSessionCategoryOptions categoryOptions;
```

#### Discussion

You use category options to tailor the behavior of the active audio session category. See [`AVAudioSession.CategoryOptions`](./categoryoptions-swift.struct.md) for the supported values.

## See Also

### Inspecting the category configuration
- [var category: AVAudioSession.Category](./category-swift.property.md)
  The current audio session category.
- [var availableCategories: [AVAudioSession.Category]](./availablecategories.md)
  The audio session categories available on the current device.
- [AVAudioSession.Category](./category-swift.struct.md)
  Audio session category identifiers.
- [AVAudioSession.CategoryOptions](./categoryoptions-swift.struct.md)
  Constants that specify optional audio behaviors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/categoryoptions-swift.property)*