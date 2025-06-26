# Declared Age Range

**Framework**: Declared Age Range  
**Kind**: module

Create age-appropriate experiences in your app by asking people to share their age range.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

#### Overview

Use the Declared Age Range framework to request people to share their age range with your app. For children in a Family Sharing group, a Family Organizer can decide whether to always share a child’s age information with your app, ask the child every time, or never share their age information. Along with an age range, the system returns an [`AgeRangeService.AgeRangeDeclaration`](agerangeservice/agerangedeclaration.md) for the age range a person provides.

## Topics

### Essentials
- [com.apple.developer.declared-age-range](../BundleResources/Entitlements/com.apple.developer.declared-age-range.md)
  A Boolean value indicating whether your app may request a person’s age range.
### Age range requests
- [struct AgeRangeService](agerangeservice.md)
  A request for the age range of a person logged onto iCloud on the device.
- [struct DeclaredAgeRangeAction](declaredagerangeaction.md)
  Provides an action to request a person’s declared age range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/DeclaredAgeRange)*