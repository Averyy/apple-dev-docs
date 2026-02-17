# farFieldInput

**Framework**: AVFAudio  
**Kind**: property

This option should be used if a session prefers to use FarFieldInput when available. This option is only valid with categories that support input - [`playAndRecord`](avaudiosession/category-swift.struct/playandrecord.md) and [`record`](avaudiosession/category-swift.struct/record.md).

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+

## Declaration

```swift
static var farFieldInput: AVAudioSession.CategoryOptions { get }
```

#### Discussion

- This option requires `AVAudioSessionCategoryOptionAllowBluetoothHFP` to be set. Otherwise error will be returned.
- Support for this can be queried on input ports via the BluetoothMicrophone interface on a port, via its member `farFieldCapture.isSupported`.
- Active sessions can see if far-field input is enabled on a bluetooth audio device by querying the BluetoothMicrophone interface of the input port of the current route for: `farFieldCapture.isEnabled`.

## See Also

- [var category: AVAudioSession.Category](avaudiosession/category-swift.property.md)
  The current audio session category.
- [var availableCategories: [AVAudioSession.Category]](avaudiosession/availablecategories.md)
  The audio session categories available on the current device.
- [AVAudioSession.Category](avaudiosession/category-swift.struct.md)
  Audio session category identifiers.
- [var categoryOptions: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.property.md)
  The set of options associated with the current audio session category.
- [AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct.md)
  Constants that specify optional audio behaviors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/categoryoptions-swift.struct/farfieldinput)*