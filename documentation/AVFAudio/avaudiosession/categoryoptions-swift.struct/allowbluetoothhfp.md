# allowBluetoothHFP

**Framework**: AVFAudio  
**Kind**: property

Allows an application to change the default behavior of some audio session categories with regard to whether Bluetooth Hands-Free Profile (HFP) devices are available for routing. The exact behavior depends on the category.

**Availability**:
- iOS 1.0+
- iPadOS 1.0+
- Mac Catalyst 13.1+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
static var allowBluetoothHFP: AVAudioSession.CategoryOptions { get }
```

#### Discussion

- [`playAndRecord`](avaudiosession/category-swift.struct/playandrecord.md): AllowBluetoothHFP defaults to false, but can be set to true, allowing a paired bluetooth HFP device to appear as an available route for input, while playing through the category-appropriate output.
- [`record`](avaudiosession/category-swift.struct/record.md): AllowBluetoothHFP defaults to false, but can be set to true, allowing a paired Bluetooth HFP device to appear as an available route for input.
- Other categories: AllowBluetoothHFP defaults to false and cannot be changed. Enabling Bluetooth for input in these categories is not allowed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/categoryoptions-swift.struct/allowbluetoothhfp)*