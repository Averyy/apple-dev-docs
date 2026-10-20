# CMVideoFormatDescriptionGetHEVCParameterSetAtIndex(_:parameterSetIndex:parameterSetPointerOut:parameterSetSizeOut:parameterSetCountOut:nalUnitHeaderLengthOut:)

**Framework**: Core Media  
**Kind**: func

Returns a parameter set contained in an HEVC (H.265) format description.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMVideoFormatDescriptionGetHEVCParameterSetAtIndex(_ videoDesc: CMFormatDescription, parameterSetIndex: Int, parameterSetPointerOut: UnsafeMutablePointer<UnsafePointer<UInt8>?>?, parameterSetSizeOut: UnsafeMutablePointer<Int>?, parameterSetCountOut: UnsafeMutablePointer<Int>?, nalUnitHeaderLengthOut NALUnitHeaderLengthOut: UnsafeMutablePointer<Int32>?) -> OSStatus
```

## See Also

- [func CMTimeFoldIntoRange(CMTime, foldRange: CMTimeRange) -> CMTime](cmtimefoldintorange(_:foldrange:).md)
  Folds a time into a time range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmvideoformatdescriptiongethevcparametersetatindex(_:parametersetindex:parametersetpointerout:parametersetsizeout:parametersetcountout:nalunitheaderlengthout:))*