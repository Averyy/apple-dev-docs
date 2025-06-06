# setupPanel(_:deviceCouldBeTarget:)

**Framework**: Objective-C Runtime  
**Kind**: method

Allows the delegate to determine if device can be used as a target.

**Availability**:
- macOS ?+

## Declaration

```swift
func setupPanel(_ aPanel: DRSetupPanel!, deviceCouldBeTarget device: DRDevice!) -> Bool
```

#### Return Value

 `YES` if the device is acceptable, `NO` if not.

#### Discussion

This method is used to limit the menu to only those devices that you want to appear.  For example, a DVD burning application might use this to limit the menu to only devices that are capable of writing DVD-Rs.

## Parameters

- `aPanel`: The panel.
- `device`: The candidate device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setuppanel(_:devicecouldbetarget:))*