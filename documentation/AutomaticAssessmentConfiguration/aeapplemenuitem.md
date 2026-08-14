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
- [static let appStore: AEAppleMenuItem](aeapplemenuitem/appstore.md)
- [static let forceQuit: AEAppleMenuItem](aeapplemenuitem/forcequit.md)
- [static let location: AEAppleMenuItem](aeapplemenuitem/location.md)
- [static let lockScreen: AEAppleMenuItem](aeapplemenuitem/lockscreen.md)
- [static let logout: AEAppleMenuItem](aeapplemenuitem/logout.md)
- [static let recent: AEAppleMenuItem](aeapplemenuitem/recent.md)
- [static let restart: AEAppleMenuItem](aeapplemenuitem/restart.md)
- [static let shutDown: AEAppleMenuItem](aeapplemenuitem/shutdown.md)
- [static let sleep: AEAppleMenuItem](aeapplemenuitem/sleep.md)
- [static let systemInformation: AEAppleMenuItem](aeapplemenuitem/systeminformation.md)
- [static let systemSettings: AEAppleMenuItem](aeapplemenuitem/systemsettings.md)

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeapplemenuitem)*