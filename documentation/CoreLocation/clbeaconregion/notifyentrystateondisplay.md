# notifyEntryStateOnDisplay

**Framework**: Core Location  
**Kind**: property

A Boolean value that indicates whether Core Location sends beacon notifications when the device’s display is on.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
var notifyEntryStateOnDisplay: Bool { get set }
```

#### Discussion

When you set this to [`true`](https://developer.apple.com/documentation/Swift/true), the location manager sends beacon notifications when the user turns on the display and the device is already inside the region. These are notifications the framework sends even if your app isn’t running. In that situation, the system launches your app into the background so that it can handle the notifications. In both situations, the location manager calls the [`locationManager(_:didDetermineState:for:)`](cllocationmanagerdelegate/locationmanager(_:diddeterminestate:for:).md) method of its delegate object.

The default value for this property is [`false`](https://developer.apple.com/documentation/Swift/false).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbeaconregion/notifyentrystateondisplay)*