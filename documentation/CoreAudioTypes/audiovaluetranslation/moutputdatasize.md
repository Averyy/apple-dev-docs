# mOutputDataSize

**Framework**: Core Audio Types  
**Kind**: property  
**Role**: Instance Property

The number of bytes in the buffer pointed at by `mOutputData`.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var mOutputDataSize: UInt32
```

```c
UInt32 mOutputDataSize;
```

## See Also

### Instance Properties
- [var mInputData: UnsafeMutableRawPointer](./minputdata.md)
  The buffer containing the data to be translated.
- [var mInputDataSize: UInt32](./minputdatasize.md)
  The number of bytes in the buffer pointed at by `mInputData`.
- [var mOutputData: UnsafeMutableRawPointer](./moutputdata.md)
  The buffer to hold the result of the translation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiovaluetranslation/moutputdatasize)*