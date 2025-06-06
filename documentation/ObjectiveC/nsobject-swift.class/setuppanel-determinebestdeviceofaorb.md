# setupPanel(_:determineBestDeviceOfA:orB:)

**Framework**: Objective-C Runtime  
**Kind**: method

Allows the delegate to specify which device is its preferred.

**Availability**:
- macOS ?+

## Declaration

```swift
func setupPanel(_ aPanel: DRSetupPanel!, determineBestDeviceOfA deviceA: DRDevice!, orB device: DRDevice!) -> DRDevice!
```

#### Return Value

 One of the two device objects passed in.

#### Discussion

When the setup panel is first displayed and again, each time a new device appears, the setup panel will ask the delegate to compare two devices to determine which is most suitable for their content to burn.

## Parameters

- `aPanel`: The panel.
- `deviceA`: A candidate device. May be nil.
- `device`: A candidate device. May be nil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setuppanel(_:determinebestdeviceofa:orb:))*