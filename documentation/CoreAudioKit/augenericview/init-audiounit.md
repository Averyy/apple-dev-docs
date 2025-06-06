# init(audioUnit:)

**Framework**: CoreAudioKit  
**Kind**: init

Creates a generic view for an audio unit, setting all display flags.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
init(audioUnit au: AudioUnit)
```

#### Return Value

The initialized generic view. On error, returns `nil`.

## Parameters

- `au`: The audio unit associated with the generic view.

## See Also

- [init(audioUnit: AudioUnit, displayFlags: AUGenericViewDisplayFlags)](augenericview/init(audiounit:displayflags:).md)
  Initializes a generic view for an audio unit, setting specific display flags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiokit/augenericview/init(audiounit:))*