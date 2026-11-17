# instrumentClusterController(_:didChangeCompassSetting:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the delegate to adjust how your app displays compass information.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
optional func instrumentClusterController(_ instrumentClusterController: CPInstrumentClusterController, didChangeCompassSetting compassSetting: CPInstrumentClusterSetting)
```

```objc
- (void) instrumentClusterController:(CPInstrumentClusterController *) instrumentClusterController didChangeCompassSetting:(CPInstrumentClusterSetting) compassSetting;
```

## Discussion

Some vehicles can ask your app to display the current compass heading along with the app’s other content. Use this method to either show or hide the information based on the provided setting value.

## Parameters

- `instrumentClusterController`: The controller object with the new setting.
- `compassSetting`: The new setting to apply to your content.

## See Also

### Responding to setting changes
- [func instrumentClusterController(CPInstrumentClusterController, didChangeSpeedLimitSetting: CPInstrumentClusterSetting)](./instrumentclustercontroller%28_,didchangespeedlimitsetting%29.md)
  Tells the delegate to adjust how your app displays speed limit information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinstrumentclustercontrollerdelegate/instrumentclustercontroller(_:didchangecompasssetting:))*