# init(audioUnit:)

**Framework**: CoreAudioKit  
**Kind**: init  
**Role**: Initializer

Creates a panner view for an audio unit.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init(audioUnit au: AudioUnit)
```

```objc
+ (AUPannerView *) AUPannerViewWithAudioUnit:(AudioUnit) au;
```

#### Return Value

The newly instantiated panner view. On error, returns `nil`.

#### Discussion

Call this static constructor as follows:

```objc
AUPannerView *mGenericPannerView = nil;
mGenericPannerView = [AUPannerView AUPannerViewWithAudioUnit: mCurrentAU];
```

## Parameters

- `au`: The panner audio unit associated with the panner view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiokit/aupannerview/init(audiounit:))*