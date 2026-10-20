# AudioConverterInputDataProc

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

Deprecated. Use [`AudioConverterFillComplexBuffer(_:_:_:_:_:_:)`](./audioconverterfillcomplexbuffer%28_,_,_,_,_,_%29.md) instead.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
typealias AudioConverterInputDataProc = (AudioConverterRef, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UnsafeMutableRawPointer>, UnsafeMutableRawPointer?) -> OSStatus
```

```c
typedef int (*)(struct OpaqueAudioConverter *, unsigned int *, void **, void *) AudioConverterInputDataProc;
```

#### Discussion

If you named your callback function `MyAudioConverterInputDataProc`, you would declare it like this:

##### Discussion

This deprecated callback supplies input data to the [`AudioConverterFillBuffer`](./audioconverterfillbuffer.md) function. Use [`AudioConverterComplexInputDataProc`](./audioconvertercomplexinputdataproc.md) instead.

## See Also

### Callbacks
- [typealias AudioConverterComplexInputDataProc](./audioconvertercomplexinputdataproc.md)
  Supplies input data to the [`AudioConverterFillComplexBuffer(_:_:_:_:_:_:)`](./audioconverterfillcomplexbuffer%28_,_,_,_,_,_%29.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioconverterinputdataproc)*