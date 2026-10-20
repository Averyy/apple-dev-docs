# isEligibleForGroupSession

**Framework**: Group Activities  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the system can start a group session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@Published
<Bool> final var isEligibleForGroupSession: Bool { get }
```

## Mentions

- [Configure your visionOS app for sharing with people nearby](../configure-your-app-for-sharing-with-people-nearby.md)
- [Presenting SharePlay activities from your app’s UI](../promoting-shareplay-activities-from-your-apps-ui.md)

#### Discussion

This property indicates whether a FaceTime call is active and the system can create group sessions. Configure a subscriber to this property to monitor changes to the system’s state. When the system can create group sessions, it sets the value of this property to `true`. When the creation of a group session isn’t possible, the system sets the value to `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupstateobserver/iseligibleforgroupsession)*