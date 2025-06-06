# AudioUnitCocoaViewInfo

**Framework**: Audio Toolbox  
**Kind**: struct

The name and number of custom Cocoa views for an audio unit.

**Availability**:
- macOS ?+

## Declaration

```swift
struct AudioUnitCocoaViewInfo
```

## Topics

### Initializers
- [init(mCocoaAUViewBundleLocation: Unmanaged<CFURL>, mCocoaAUViewClass: Unmanaged<CFString>)](audiounitcocoaviewinfo/init(mcocoaauviewbundlelocation:mcocoaauviewclass:).md)
### Instance Properties
- [var mCocoaAUViewBundleLocation: Unmanaged<CFURL>](audiounitcocoaviewinfo/mcocoaauviewbundlelocation.md)
- [var mCocoaAUViewClass: Unmanaged<CFString>](audiounitcocoaviewinfo/mcocoaauviewclass.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [func GetAudioUnitParameterDisplayType(AudioUnitParameterOptions) -> AudioUnitParameterOptions](getaudiounitparameterdisplaytype(_:).md)
- [func SetAudioUnitParameterDisplayType(AudioUnitParameterOptions, AudioUnitParameterOptions) -> AudioUnitParameterOptions](setaudiounitparameterdisplaytype(_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitcocoaviewinfo)*