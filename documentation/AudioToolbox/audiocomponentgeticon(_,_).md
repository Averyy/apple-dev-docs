# AudioComponentGetIcon(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

The UIImage of the audio component’s icon.

**Availability**:
- iOS 7.0+ - Deprecated in 14.0 (renamed: AudioComponentCopyIcon(_:))
- iPadOS 7.0+ - Deprecated in 14.0 (renamed: AudioComponentCopyIcon(_:))
- Mac Catalyst 14.0+ - Deprecated in 14.0 (renamed: AudioComponentCopyIcon(_:))
- macOS 10.11+ - Deprecated in 11.0 (renamed: AudioComponentCopyIcon(_:))
- tvOS 9.0+ - Deprecated in 14.0 (renamed: AudioComponentCopyIcon(_:))
- visionOS 1.0+ - Deprecated in 1.0 (renamed: AudioComponentCopyIcon(_:))

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
func AudioComponentGetIcon(_ comp: AudioComponent, _ desiredPointSize: Float) -> UIImage?
```

*macOS*

```swift
func AudioComponentGetIcon(_ comp: AudioComponent) -> NSImage?
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```c
extern UIImage *AudioComponentGetIcon(AudioComponent comp, float desiredPointSize);
```

*Mac Catalyst*

```c
static UIImage *AudioComponentGetIcon(AudioComponent comp, float desiredPointSize);
```

*macOS*

```c
extern NSImage *AudioComponentGetIcon(AudioComponent comp);
```

## See Also

### Inter-App Audio
- [func AudioOutputUnitPublish(UnsafePointer<AudioComponentDescription>, CFString, UInt32, AudioUnit) -> OSStatus](./audiooutputunitpublish%28_,_,_,_%29.md)
  Registers an audio output unit for use by other applications.
- [func AudioOutputUnitGetHostIcon(AudioUnit, Float) -> UIImage?](./audiooutputunitgethosticon%28_,_%29.md)
  The host app’s icon.
- [func AudioComponentGetLastActiveTime(AudioComponent) -> CFAbsoluteTime](./audiocomponentgetlastactivetime%28_%29.md)
  The time at which the application publishing the component was last active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentgeticon(_:_:))*