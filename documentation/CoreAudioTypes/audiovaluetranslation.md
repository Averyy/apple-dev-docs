# AudioValueTranslation

**Framework**: Core Audio Types  
**Kind**: struct

A structure that stores buffers to use in translation operations.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- macOS 10.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
struct AudioValueTranslation
```

## Topics

### Initializers
- [init(mInputData: UnsafeMutableRawPointer, mInputDataSize: UInt32, mOutputData: UnsafeMutableRawPointer, mOutputDataSize: UInt32)](audiovaluetranslation/init(minputdata:minputdatasize:moutputdata:moutputdatasize:).md)
### Instance Properties
- [var mInputData: UnsafeMutableRawPointer](audiovaluetranslation/minputdata.md)
  The buffer containing the data to be translated.
- [var mInputDataSize: UInt32](audiovaluetranslation/minputdatasize.md)
  The number of bytes in the buffer pointed at by `mInputData`.
- [var mOutputData: UnsafeMutableRawPointer](audiovaluetranslation/moutputdata.md)
  The buffer to hold the result of the translation.
- [var mOutputDataSize: UInt32](audiovaluetranslation/moutputdatasize.md)
  The number of bytes in the buffer pointed at by `mOutputData`.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct AudioValueRange](audiovaluerange.md)
  A structure that represents a continuous range of values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiovaluetranslation)*