# GroupStateObserver

**Framework**: Group Activities  
**Kind**: class

An object that contains information about the system’s ability to start SharePlay experiences.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
final class GroupStateObserver
```

## Mentions

- [Presenting SharePlay activities from your app’s UI](promoting-shareplay-activities-from-your-apps-ui.md)

#### Overview

Starting a SharePlay experience with the Group Activities framework requires an active FaceTime call. Use a `GroupStateObserver` object to determine whether it’s possible to start such an experience. When no call is active, you might adjust your app’s user interface. For example, you might hide or remove controls that start a shared activity.

To get the current system state, create a `GroupStateObserver` object and check the value of its [`isEligibleForGroupSession`](groupstateobserver/iseligibleforgroupsession.md) property. To respond right away when the value of the property changes, configure a subscriber for that property.

## Topics

### Creating a group state observer
- [convenience init()](groupstateobserver/init.md)
  Creates a new group state observer object for determining the availability of group sessions.
### Determining the eligibility for shared activities
- [var isEligibleForGroupSession: Bool](groupstateobserver/iseligibleforgroupsession.md)
  A Boolean value that indicates whether the system can start a group session.
### Instance Properties
- [var $isEligibleForGroupSession: Published<Bool>.Publisher](groupstateobserver/$iseligibleforgroupsession.md)
### Type Aliases
- [GroupStateObserver.ObjectWillChangePublisher](groupstateobserver/objectwillchangepublisher.md)
  The type of publisher that emits before the object has changed.
### Default Implementations
- [ObservableObject Implementations](groupstateobserver/observableobject-implementations.md)

## Relationships

### Conforms To
- [ObservableObject](../Combine/ObservableObject.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupstateobserver)*