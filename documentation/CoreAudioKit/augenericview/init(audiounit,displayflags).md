# init(audioUnit:displayFlags:)

**Framework**: CoreAudioKit  
**Kind**: init  
**Role**: Initializer

Initializes a generic view for an audio unit, setting specific display flags.

**Availability**:
- macOS 10.4+

## Declaration

```swift
init(audioUnit inAudioUnit: AudioUnit, displayFlags inFlags: AUGenericViewDisplayFlags)
```

```objc
- (AUGenericView *) initWithAudioUnit:(AudioUnit) inAudioUnit displayFlags:(AUGenericViewDisplayFlags) inFlags;
```

#### Return Value

The initialized audio unit associated with the generic view, with display flags set.

## Parameters

- `inAudioUnit`: The audio unit associated with the generic view.
- `inFlags`: One or more flags that specify display properties. You can combine multiple flags using the logical `OR` (`|`) operator. For the available flags, see `Generic View Display Flags`.

## Topics

### Display Flags
- [struct AUGenericViewDisplayFlags](../augenericviewdisplayflags.md)
  Flags that describe the display of a generic view.

## See Also

### Creating a Generic View
- [init(audioUnit: AudioUnit)](./init%28audiounit%29.md)
  Creates a generic view for an audio unit, setting all display flags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiokit/augenericview/init(audiounit:displayflags:))*