# audioUnit

**Framework**: CoreAudioKit  
**Kind**: property  
**Role**: Instance Property

The audio unit associated with the generic view.

**Availability**:
- macOS 10.4+

## Declaration

```swift
var audioUnit: AudioUnit { get }
```

```objc
@property (readonly) AudioUnit audioUnit;
```

## Discussion

The audio unit associated with the generic view. On error, returns `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiokit/augenericview/audiounit)*