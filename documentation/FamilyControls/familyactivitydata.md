# FamilyActivityData

**Framework**: Family Controls  
**Kind**: class

An interface to the user’s family activity data.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
class FamilyActivityData
```

#### Overview

To fetch a user’s family activity data, use [`installedApplications`](familyactivitydata/installedapplications.md), [`visitedWebDomains`](familyactivitydata/visitedwebdomains.md) or [`activityCategories`](familyactivitydata/activitycategories.md) based on the type of data you’re interested in.

> ❗ **Important**: You must add the Family Controls App & Website Usage capability to your app before you attempt to access variables on this class. This capability adds the doc://com.apple.documentation/documentation/bundleresources/entitlements/com_apple_developer_family-controls_app-and-website-usage to your app. In a compatible iPad or iPhone app running in visionOS or macOS, attempts to fetch user data always fail. For more information, see [`Adding capabilities to your app`](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app). Additionally, your app must be authorized with data access via [`AuthorizationCenter`](authorizationcenter.md) before attempting to fetch data. If your app is not authorized with data access, the attempt will always fail.

## Topics

### Instance Properties
- [var activityCategories: Set<ActivityCategory>](familyactivitydata/activitycategories.md)
  The set of all possible activity categories.
- [var installedApplications: [Application]](familyactivitydata/installedapplications.md)
  An array of applications installed by the current user.
- [var visitedWebDomains: [WebDomain]](familyactivitydata/visitedwebdomains.md)
  An array of web domains visited by the current user.
### Type Properties
- [static let shared: FamilyActivityData](familyactivitydata/shared.md)
  The shared Family Activity Data instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitydata)*