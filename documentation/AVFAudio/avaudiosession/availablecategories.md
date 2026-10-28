# availableCategories

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The audio session categories available on the current device.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var availableCategories: [AVAudioSession.Category] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSString *> * availableCategories;
```

## Discussion

Not every device supports every audio session category. For instance, the [`record`](./category-swift.struct/record.md) category isn’t available on a device that doesn’t support audio input.

Query this property to determine if the category you’d like to use is available on the current device.

## See Also

### Inspecting the category configuration
- [var category: AVAudioSession.Category](./category-swift.property.md)
  The current audio session category.
- [AVAudioSession.Category](./category-swift.struct.md)
  Audio session category identifiers.
- [var categoryOptions: AVAudioSession.CategoryOptions](./categoryoptions-swift.property.md)
  The set of options associated with the current audio session category.
- [AVAudioSession.CategoryOptions](./categoryoptions-swift.struct.md)
  Constants that specify optional audio behaviors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/availablecategories)*