# activityData(filteredBy:using:)

**Framework**: Device Activity  
**Kind**: method  
**Role**: Type Method

Requests device activity data using a filter.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
static func activityData(filteredBy filter: DeviceActivityFilter = .init(), using policy: DeviceActivityData.Policy = .cached) -> some AsyncSequence<DeviceActivityData, any Error>
```

#### Return Value

A sequence of device activity data for the given filter.

#### Discussion

Use this method to export family activity data, for use in another app or platform.

##### Region support, authorization, and entitlement

You can develop and test an app that uses this method on devices in any region. Customer installations of your app can only use the method on devices located in the EU that are signed in with an Apple Account with an EU country or region. Otherwise, it throws an error.

Your app’s authorization status needs to be [`AuthorizationStatus.approvedWithDataAccess`](../../FamilyControls/authorizationstatus/approvedwithdataaccess.md) to use this method.

Your app needs the  [`Family Controls App and Website Usage`](../../BundleResources/entitlements/com.apple.developer.family-controls.app-and-website-usage.md) entitlement to use this method. Enable the capability on your Xcode target to add the entitlement to your app. For more information, see [Adding capabilities to your app](../../Xcode/adding-capabilities-to-your-app.md).

## Parameters

- `filter`: The filter to use when fetching activity data.
- `policy`: The policy to use when fetching activity data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/activitydata(filteredby:using:))*