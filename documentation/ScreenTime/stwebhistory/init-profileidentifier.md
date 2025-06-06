# init(profileIdentifier:)

**Framework**: Screen Time  
**Kind**: init

Creates a web history instance to delete web-usage data associated to the profile identifier you specify.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+

## Declaration

```swift
init(profileIdentifier: STWebHistory.ProfileIdentifier?)
```

#### Discussion

The default value for `profileIdentifier` is `nil`. This identifier can be used to delete browsing history for a specific profile. Using `nil` will only delete web history reported without a profile identifier.

## Parameters

- `profileIdentifier`: The identifier of the current browsing profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screentime/stwebhistory/init(profileidentifier:))*