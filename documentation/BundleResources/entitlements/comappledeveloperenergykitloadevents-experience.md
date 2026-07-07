# EnergyKit LoadEvents Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias

An entitlement that works with the EnergyKit framework to share energy data and usage insights in the Home app.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)



**Type**: boolean

**Default**: `NO`

#### Discussion

When you adopt this entitlement, the framework displays device names and energy usage context in the Home app. The information derives from the two load events, [`ElectricVehicleLoadEvent`](https://developer.apple.com/documentation/EnergyKit/ElectricVehicleLoadEvent) and [`ElectricHVACLoadEvent`](https://developer.apple.com/documentation/EnergyKit/ElectricHVACLoadEvent), that your app submits to the system. The Home app displays the data in the form of activity logs, historical charts, and trend notifications.

To enable this entitlement, add the EnergyKit LoadEvents capability and the base EnergyKit capability (see [`EnergyKit Entitlement`](entitlements/com.apple.developer.energykit.md)) to your app’s target in Xcode.

For more information, see [`Adding capabilities to your app`](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app).

## See Also

- [EnergyKit Entitlement](entitlements/com.apple.developer.energykit.md)
  The entitlement the system requires for an app to use the EnergyKit framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.energykit.loadevents-experience)*