# CMTimeFoldIntoRange(_:foldRange:)

**Framework**: Core Media  
**Kind**: func

Folds a time into a time range.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMTimeFoldIntoRange(_ time: CMTime, foldRange: CMTimeRange) -> CMTime
```

#### Return Value

A time that represents the translated duration.

## Parameters

- `time`: The time to fold.
- `foldRange`: The time range into which to fold the time.

## See Also

- [func CMVideoFormatDescriptionGetHEVCParameterSetAtIndex(CMFormatDescription, parameterSetIndex: Int, parameterSetPointerOut: UnsafeMutablePointer<UnsafePointer<UInt8>?>?, parameterSetSizeOut: UnsafeMutablePointer<Int>?, parameterSetCountOut: UnsafeMutablePointer<Int>?, nalUnitHeaderLengthOut: UnsafeMutablePointer<Int32>?) -> OSStatus](cmvideoformatdescriptiongethevcparametersetatindex(_:parametersetindex:parametersetpointerout:parametersetsizeout:parametersetcountout:nalunitheaderlengthout:).md)
  Returns a parameter set contained in an HEVC (H.265) format description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimefoldintorange(_:foldrange:))*