# notifyEntryStateOnDisplay

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether Core Location sends beacon notifications when the device’s display is on.

**Availability**:
- iOS 7.0+ - Deprecated in 27.2
- iPadOS 7.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2

## Declaration

```swift
var notifyEntryStateOnDisplay: Bool { get set }
```

```objc
@property (atomic, assign) BOOL notifyEntryStateOnDisplay;
```

#### Discussion

When you set this to [`true`](../../Swift/true.md), the location manager sends beacon notifications when the user turns on the display and the device is already inside the region. These are notifications the framework sends even if your app isn’t running. In that situation, the system launches your app into the background so that it can handle the notifications. In both situations, the location manager calls the [`locationManager(_:didDetermineState:for:)`](../cllocationmanagerdelegate/locationmanager%28_,diddeterminestate,for%29.md) method of its delegate object.

The default value for this property is [`false`](../../Swift/false.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbeaconregion/notifyentrystateondisplay)*