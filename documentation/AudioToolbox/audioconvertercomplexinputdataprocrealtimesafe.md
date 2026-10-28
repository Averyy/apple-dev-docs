# AudioConverterComplexInputDataProcRealtimeSafe

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
typealias AudioConverterComplexInputDataProcRealtimeSafe = (AudioConverterRef, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<UnsafeMutablePointer<AudioStreamPacketDescription>?>?, UnsafeMutableRawPointer?) -> OSStatus
```

```c
typedef int (*)(struct OpaqueAudioConverter *, unsigned int *, struct AudioBufferList *, struct AudioStreamPacketDescription **, void *) __attribute__((nonblocking)) AudioConverterComplexInputDataProcRealtimeSafe;
```

## Discussion

Realtime-safe variant of AudioConverterComplexInputDataProc.

See the discussions of AudioConverterComplexInputDataProc and AudioConverterFillComplexBuffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioconvertercomplexinputdataprocrealtimesafe)*