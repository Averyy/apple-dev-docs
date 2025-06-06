# setupPanel(_:deviceContainsSuitableMedia:promptString:)

**Framework**: Objective-C Runtime  
**Kind**: method

This delegate method allows the delegate to determine if the media inserted in the device is suitable for whatever operation is to be performed.

**Availability**:
- macOS ?+

## Declaration

```swift
func setupPanel(_ aPanel: DRSetupPanel!, deviceContainsSuitableMedia device: DRDevice!, promptString prompt: AutoreleasingUnsafeMutablePointer<NSString?>!) -> Bool
```

#### Return Value

 Return `NO` to disable the default button.

## Parameters

- `aPanel`: The panel.
- `device`: The device that contains the media being asked about.
- `prompt`: 	A pointer to storage for an NSString. Pass back an NSString object describing the media state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setuppanel(_:devicecontainssuitablemedia:promptstring:))*