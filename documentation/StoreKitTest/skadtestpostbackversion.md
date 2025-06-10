# SKAdTestPostbackVersion

**Framework**: StoreKit Test  
**Kind**: struct

A constant that indicates the postback version.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
struct SKAdTestPostbackVersion
```

#### Overview

This postback version number corresponds to a version of SKAdNetwork. All versions of [`SKAdNetwork`](https://developer.apple.com/documentation/StoreKit/SKAdNetwork) have specific instructions for signing ads and validating postbacks. The testing environment supports testing the versions indicated by the constants listed in the Getting SKAdNetwork Versions section below.

For more information about versions, see [`SKAdNetwork release notes`](https://developer.apple.com/documentation/StoreKit/skadnetwork-release-notes).

## Topics

### Getting SKAdNetwork Versions
- [static let version4_0: SKAdTestPostbackVersion](skadtestpostbackversion/version4_0.md)
  A constant that represents SKAdNetwork version 4.0.
- [static let version3_0: SKAdTestPostbackVersion](skadtestpostbackversion/version3_0.md)
  A constant that represents SKAdNetwork version 3.0.
- [static let version2_2: SKAdTestPostbackVersion](skadtestpostbackversion/version2_2.md)
  A constant that represents SKAdNetwork version 2.2.
- [static let version2_1: SKAdTestPostbackVersion](skadtestpostbackversion/version2_1.md)
  A constant that represents SKAdNetwork version 2.1.
### Initializing the Postback Version
- [init(rawValue: String)](skadtestpostbackversion/init(rawvalue:).md)
  Initialize a version object with the supplied raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Testing and validating ad impression signatures and postbacks for SKAdNetwork](testing-and-validating-ad-impression-signatures-and-postbacks-for-skadnetwork.md)
  Validate your ad impressions and test your postbacks by creating unit tests using the StoreKit Test framework.
- [class SKAdTestSession](skadtestsession.md)
  The class you use to test ad impressions and postbacks in Xcode.
- [class SKAdTestPostback](skadtestpostback.md)
  A test postback that contains ad conversion information in the testing environment.
- [class SKAdTestPostbackResponse](skadtestpostbackresponse.md)
  The status and error information for a postback that the system sends in the testing environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestpostbackversion)*