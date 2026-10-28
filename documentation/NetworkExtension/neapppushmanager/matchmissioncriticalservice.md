# matchMissionCriticalService

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

A property that indicates support for Mission Critical Services.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
var matchMissionCriticalService: Bool { get set }
```

```objc
@property BOOL matchMissionCriticalService;
```

## Discussion

Set this property to `true` (Swift) or `YES` (Obj-C) in your container app to use 3GPP Mission Critical Services (MCX). On supported cellular networks, this allows Push to Talk apps to meet the 3GPP MCX’s performance and latency standards by using the Mission Critical Service slice.

When you use this property in your containing app, the system runs the `NEAppPushProvider` if both of the following criteria are met:

- The container app has both the Local Push Connectivity entitlement and the Mission Critical Service application category entitlements. For the former, use [`Network Extensions Entitlement`](../../BundleResources/entitlements/com.apple.developer.networking.networkextension.md) with a value of `app-push-provider`. For the latter, use [`5G Network Slicing App Category`](../../BundleResources/entitlements/com.apple.developer.networking.slicing.appcategory.md) with a value of `mc-9500`.
- The device has a cellular plan that supports Mission Critical Services.

After the app push extension launches, the extension establishes a network connection to its backend server using the MCX network slice. The framework delivers incoming Push to Talk messages with the [`reportPushToTalkMessage(userInfo:)`](../neapppushprovider/reportpushtotalkmessage%28userinfo%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapppushmanager/matchmissioncriticalservice)*