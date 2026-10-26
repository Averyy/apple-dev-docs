# AudioConverterFillBuffer

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.1+ - Deprecated in 10.5

> **Deprecated**: Deprecated. Use [`AudioConverterFillComplexBuffer(_:_:_:_:_:_:)`](./audioconverterfillcomplexbuffer%28_,_,_,_,_,_%29.md) instead.

## Declaration

```c
extern OSStatus AudioConverterFillBuffer(AudioConverterRef inAudioConverter, AudioConverterInputDataProc inInputDataProc, void *inInputDataProcUserData, UInt32 *ioOutputDataSize, void *outOutputData);
```

#### Return Value

A  result code.

#### Discussion

Converts audio data supplied by a callback function.

##### Special Considerations

This function is deprecated. Use the [`AudioConverterFillComplexBuffer(_:_:_:_:_:_:)`](./audioconverterfillcomplexbuffer%28_,_,_,_,_,_%29.md) function instead.

## Parameters

- `inAudioConverter`: The audio converter to use for format conversion.
- `inInputDataProc`: A callback function that supplies audio data to convert. This callback is invoked repeatedly as the converter is ready for new input data.
- `inInputDataProcUserData`: Custom data for use by your application when receiving a callback invocation.
- `ioOutputDataSize`: On input, the size, in bytes, of the buffer available for the converted data. On output, the number of bytes written to the output buffer (pointed to by the `outOutputData` parameter).
- `outOutputData`: On output, the converted audio data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioconverterfillbuffer)*