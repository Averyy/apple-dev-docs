# com.apple.developer.healthkit.research

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether an approved health research app offers only Full Access when it requests HealthKit read access.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- visionOS 27.2+
- watchOS 27.2+



**Type**: boolean

#### Discussion

In iOS 27 and later, HealthKit allows people to choose between two options when they share data with an app: **Past 30 Days and Future Data** and **All Recorded Data and Future Data**. Apps with this entitlement offer only Full Access for people to approve or deny, without the **Past 30 Days and Future Data** option. HealthKit periodically reminds people that an app can read their health data, but reminds them about apps with this entitlement less often.

Use this entitlement if your app is a health research app that needs uninterrupted access to HealthKit data. For example, apps that collect data from infrequent health events can’t tolerate a gap in access. Apple grants this entitlement individually to qualifying apps. To request permission to use it, see [`HealthKit Research Entitlement Request`](https://developer.apple.comhttps://developer.apple.com/contact/request/healthkit-research-entitlement).

## See Also

- [HealthKit Entitlement](entitlements/com.apple.developer.healthkit.md)
  A Boolean value that indicates whether the app may request user authorization to access health and activity data that appears in the Health app.
- [HealthKit Capabilities Entitlement](entitlements/com.apple.developer.healthkit.access.md)
  Health data types that require additional permission.
- [class BGHealthResearchTask](../backgroundtasks/bghealthresearchtask.md)
  A time-consuming, necessary processing task that runs while the app is in the background to prepare data essential to a health research study.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.healthkit.research)*