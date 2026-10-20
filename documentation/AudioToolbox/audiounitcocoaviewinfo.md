# AudioUnitCocoaViewInfo

**Framework**: Audio Toolbox  
**Kind**: struct  
**Role**: Structure

The name and number of custom Cocoa views for an audio unit.

**Availability**:
- macOS

## Declaration

```swift
struct AudioUnitCocoaViewInfo
```

```c
struct AudioUnitCocoaViewInfo;
```

## Topics

### Initializers
- [init(mCocoaAUViewBundleLocation: Unmanaged<CFURL>, mCocoaAUViewClass: Unmanaged<CFString>)](./audiounitcocoaviewinfo/init%28mcocoaauviewbundlelocation,mcocoaauviewclass%29.md)
### Instance Properties
- [var mCocoaAUViewBundleLocation: Unmanaged<CFURL>](./audiounitcocoaviewinfo/mcocoaauviewbundlelocation.md)
- [var mCocoaAUViewClass: Unmanaged<CFString>](./audiounitcocoaviewinfo/mcocoaauviewclass.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

## See Also

### Configuring the Audio Unit UI
- [func GetAudioUnitParameterDisplayType(AudioUnitParameterOptions) -> AudioUnitParameterOptions](./getaudiounitparameterdisplaytype%28_%29.md)
- [func SetAudioUnitParameterDisplayType(AudioUnitParameterOptions, AudioUnitParameterOptions) -> AudioUnitParameterOptions](./setaudiounitparameterdisplaytype%28_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitcocoaviewinfo)*