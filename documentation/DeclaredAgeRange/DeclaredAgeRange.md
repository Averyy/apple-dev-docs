# Declared Age Range

**Framework**: Declared Age Range  
**Kind**: module

Create age-appropriate experiences in your app by asking people to share their age range.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

#### Overview

Use the Declared Age Range API to request that people share their age range with your app. For children in a Family Sharing group, a parent or guardian or the Family Organizer can decide whether to always share a child’s age information with your app, ask the child every time, or never share their age information. Along with an age range, the system returns an [`AgeRangeService.AgeRangeDeclaration`](agerangeservice/agerangedeclaration.md) for the age range a person provides. To use the Declared Age Range API, add the [`com.apple.developer.declared-age-range`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.declared-age-range) entitlement to your app by enabling the Declared Age Range capability on your target in Xcode. For more information, see [`Adding capabilities to your app`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/adding-capabilities-to-your-app).

> ❗ **Important**: Data from the Declared Age Range API is based on information declared by an end user, or their parent or guardian. You are solely responsible for ensuring compliance with associated laws or regulations that may apply to your app.

## Topics

### Essentials
- [com.apple.developer.declared-age-range](../BundleResources/Entitlements/com.apple.developer.declared-age-range.md)
  A Boolean value indicating whether your app may request a person’s age range.
- [Requesting people’s age range information in your app](requesting-people-share-their-age-range-with-your-app.md)
  Ask people to share their age range with your app, and tailor features for adults, teens, and children while preserving privacy.
### Age range requests
- [struct AgeRangeService](agerangeservice.md)
  A request for the age range of a person logged onto the current device.
- [struct DeclaredAgeRangeAction](declaredagerangeaction.md)
  An action that requests a person’s age range.
### Significant change acknowledgment
- [struct SignificantUpdateAction](significantupdateaction.md)
  An action that presents a system sheet for significant app update acknowledgments.
### Articles
- [Implementing age assurance and permissions](implementing-age-assurance-and-permissions.md)
  Create a significant change flow to inform people about important updates in your app and request age-related permissions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/DeclaredAgeRange)*