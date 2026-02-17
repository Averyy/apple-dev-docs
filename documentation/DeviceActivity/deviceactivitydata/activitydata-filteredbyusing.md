# activityData(filteredBy:using:)

**Framework**: Device Activity  
**Kind**: method

Requests device activity data using a filter.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
static func activityData(filteredBy filter: DeviceActivityFilter = .init(), using policy: DeviceActivityData.Policy = .cached) -> some AsyncSequence<DeviceActivityData, any Error>
```

#### Return Value

A sequence of device activity data for the given filter.

#### Discussion

> ❗ **Important**:  You must add the Family Controls User Data capability to your app before you attempt to use this function. This capability adds the doc://com.apple.documentation/documentation/bundleresources/entitlements/com_apple_developer_family-controls-user-data to your app. In a compatible iPad or iPhone app running on visionOS or macOS, using this function will always throw. For more information, see [`Adding capabilities to your app`](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app). Additionally, your app must be authorized and data access must be available before using this function, or it will always throw. See [`AuthorizationCenter`](https://developer.apple.com/documentation/FamilyControls/AuthorizationCenter) for more details.

## Parameters

- `filter`: The filter to use when fetching activity data.
- `policy`: The policy to use when fetching activity data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/activitydata(filteredby:using:))*