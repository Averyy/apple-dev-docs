# SecTrustSettingsResult

**Framework**: Security  
**Kind**: enum

Trust settings returned in usage constraints dictionaries.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
enum SecTrustSettingsResult
```

#### Overview

These values appear in the usage constraints dictionaries returned by the [`SecTrustSettingsCopyTrustSettings(_:_:_:)`](sectrustsettingscopytrustsettings(_:_:_:).md) and [`SecTrustSettingsSetTrustSettings(_:_:_:)`](sectrustsettingssettrustsettings(_:_:_:).md) functions.

## Topics

### Constants
- [SecTrustSettingsResult.invalid](sectrustsettingsresult/invalid.md)
  Never valid in a trust settings array or in an API call.
- [SecTrustSettingsResult.trustRoot](sectrustsettingsresult/trustroot.md)
  This root certificate is explicitly trusted.
- [SecTrustSettingsResult.trustAsRoot](sectrustsettingsresult/trustasroot.md)
  This non-root certificate is explicitly trusted as if it were a trusted root.
- [SecTrustSettingsResult.deny](sectrustsettingsresult/deny.md)
  This certificate is explicitly distrusted.
- [SecTrustSettingsResult.unspecified](sectrustsettingsresult/unspecified.md)
  This certificate is neither trusted nor distrusted. This value can be used to specify an “allowed error” without assigning trust to a specific certificate.
### Initializers
- [init?(rawValue: UInt32)](sectrustsettingsresult/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustsettingsresult)*