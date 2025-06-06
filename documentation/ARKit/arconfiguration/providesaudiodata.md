# providesAudioData

**Framework**: ARKit  
**Kind**: property

A Boolean value that specifies whether to capture audio during the AR session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var providesAudioData: Bool { get set }
```

#### Discussion

To receive and handle captured audio data, your session delegate must implement the [`session(_:didOutputAudioSampleBuffer:)`](arsessionobserver/session(_:didoutputaudiosamplebuffer:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration/providesaudiodata)*