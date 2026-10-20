# init(bundleIdentifier:profileIdentifier:)

**Framework**: Screen Time  
**Kind**: init

Creates a web history instance to delete web-usage data associated to the bundle identifier and profile identifier you specify.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+

## Declaration

```swift
init(bundleIdentifier: String, profileIdentifier: STWebHistory.ProfileIdentifier?) throws
```

#### Discussion

The default value for `bundleIdentifier` is `Bundle.main.bundleIdentifier`. This is the recommended identifier to use, except for example, if a helper process is presenting web UI and you want to group that web-usage under the main app’s bundle identifier.

The default value for `profileIdentifier` is `nil`. This identifier can be used to delete browsing history for a specific profile. Using `nil` will only delete web history reported without a profile identifier.

## Parameters

- `bundleIdentifier`: The bundle identifier.
- `profileIdentifier`: The identifier of the current browsing profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screentime/stwebhistory/init(bundleidentifier:profileidentifier:))*