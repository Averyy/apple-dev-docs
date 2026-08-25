# AEAppleMenuItem

**Framework**: Automatic Assessment Configuration  
**Kind**: struct

Identifies an item in the Apple menu.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
struct AEAppleMenuItem
```

#### Overview

Use these constants with [`allowedAppleMenuItems`](aeassessmentconfiguration/allowedapplemenuitems.md) to control which Apple menu items are visible during an assessment session.

> **Note**: [`aboutThisMac`](aeapplemenuitem/aboutthismac.md) is always visible during assessment sessions regardless of configuration.

## Topics

### Initializers
- [init(rawValue: String)](aeapplemenuitem/init(rawvalue:).md)
### Type Properties
- [static let aboutThisMac: AEAppleMenuItem](aeapplemenuitem/aboutthismac.md)
  The About This Mac item, which remains visible during an assessment session whether or not [`allowedAppleMenuItems`](aeassessmentconfiguration/allowedapplemenuitems.md) names it.
- [static let appStore: AEAppleMenuItem](aeapplemenuitem/appstore.md)
  The App Store item.
- [static let forceQuit: AEAppleMenuItem](aeapplemenuitem/forcequit.md)
  The Force Quit item, covering both the Force Quit Applications window and quitting an app outright.
- [static let location: AEAppleMenuItem](aeapplemenuitem/location.md)
  The Location item.
- [static let lockScreen: AEAppleMenuItem](aeapplemenuitem/lockscreen.md)
  The Lock Screen item.
- [static let logout: AEAppleMenuItem](aeapplemenuitem/logout.md)
  The Log Out item, covering both the command and its confirmation.
- [static let recent: AEAppleMenuItem](aeapplemenuitem/recent.md)
  The Recent Items item.
- [static let restart: AEAppleMenuItem](aeapplemenuitem/restart.md)
  The Restart item, covering both the command and its confirmation.
- [static let shutDown: AEAppleMenuItem](aeapplemenuitem/shutdown.md)
  The Shut Down item, covering both the command and its confirmation.
- [static let sleep: AEAppleMenuItem](aeapplemenuitem/sleep.md)
  The Sleep item.
- [static let systemInformation: AEAppleMenuItem](aeapplemenuitem/systeminformation.md)
  The System Information item.
- [static let systemSettings: AEAppleMenuItem](aeapplemenuitem/systemsettings.md)
  The System Settings item.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeapplemenuitem)*