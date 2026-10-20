# Open

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var Open: (UnsafeMutableRawPointer, AudioComponentInstance) -> OSStatus
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```c
int (*)(void *, struct OpaqueAudioComponentInstance *) Open;
```

*macOS*

```c
int (*)(void *, struct ComponentInstanceRecord *) Open;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentplugininterface/open)*