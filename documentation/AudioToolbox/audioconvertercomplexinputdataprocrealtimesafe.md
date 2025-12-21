# AudioConverterComplexInputDataProcRealtimeSafe

**Framework**: Audio Toolbox  
**Kind**: typealias

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias AudioConverterComplexInputDataProcRealtimeSafe = (AudioConverterRef, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<UnsafeMutablePointer<AudioStreamPacketDescription>?>?, UnsafeMutableRawPointer?) -> OSStatus
```

#### Discussion

Realtime-safe variant of AudioConverterComplexInputDataProc.

See the discussions of AudioConverterComplexInputDataProc and AudioConverterFillComplexBuffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioconvertercomplexinputdataprocrealtimesafe)*