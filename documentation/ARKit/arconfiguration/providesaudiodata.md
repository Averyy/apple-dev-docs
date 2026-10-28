# providesAudioData

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that specifies whether to capture audio during the AR session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
var providesAudioData: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL providesAudioData;
```

## Discussion

To receive and handle captured audio data, your session delegate must implement the [`session(_:didOutputAudioSampleBuffer:)`](../arsessionobserver/session%28_,didoutputaudiosamplebuffer%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration/providesaudiodata)*