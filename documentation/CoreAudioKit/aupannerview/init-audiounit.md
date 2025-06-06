# init(audioUnit:)

**Framework**: CoreAudioKit  
**Kind**: init

Creates a panner view for an audio unit.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
init(audioUnit au: AudioUnit)
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