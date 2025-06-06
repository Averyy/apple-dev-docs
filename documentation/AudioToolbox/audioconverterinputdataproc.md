# AudioConverterInputDataProc

**Framework**: Audio Toolbox  
**Kind**: typealias

Deprecated. Use [`AudioConverterFillComplexBuffer(_:_:_:_:_:_:)`](audioconverterfillcomplexbuffer(_:_:_:_:_:_:).md) instead.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias AudioConverterInputDataProc = (AudioConverterRef, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UnsafeMutableRawPointer>, UnsafeMutableRawPointer?) -> OSStatus
```

#### Discussion

If you named your callback function `MyAudioConverterInputDataProc`, you would declare it like this:

##### Discussion

This deprecated callback supplies input data to the [`AudioConverterFillBuffer`](audioconverterfillbuffer.md) function. Use [`AudioConverterComplexInputDataProc`](audioconvertercomplexinputdataproc.md) instead.

## See Also

- [typealias AudioConverterComplexInputDataProc](audioconvertercomplexinputdataproc.md)
  Supplies input data to the [`AudioConverterFillComplexBuffer(_:_:_:_:_:_:)`](audioconverterfillcomplexbuffer(_:_:_:_:_:_:).md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioconverterinputdataproc)*