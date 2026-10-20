# init(audioUnit:)

**Framework**: CoreAudioKit  
**Kind**: init  
**Role**: Initializer

Creates a generic view for an audio unit, setting all display flags.

**Availability**:
- macOS 10.4+

## Declaration

```swift
init(audioUnit au: AudioUnit)
```

```objc
- (AUGenericView *) initWithAudioUnit:(AudioUnit) au;
```

#### Return Value

The initialized generic view. On error, returns `nil`.

## Parameters

- `au`: The audio unit associated with the generic view.

## See Also

### Creating a Generic View
- [init(audioUnit: AudioUnit, displayFlags: AUGenericViewDisplayFlags)](./init%28audiounit,displayflags%29.md)
  Initializes a generic view for an audio unit, setting specific display flags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiokit/augenericview/init(audiounit:))*