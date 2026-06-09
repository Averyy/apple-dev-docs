# deviceName

**Framework**: EnergyKit  
**Kind**: property

A human-readable name for the device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
var deviceName: String { get }
```

#### Discussion

Set a String value that meets these criteria:

- Less than or equal to 250 `UTF-16` characters
- Contains only alphanumeric, whitespace, punctuation, or symbol characters.
- Isn’t the empty String

The EnergyKit framework alters the value to abide by these rules, if necessary.

The Home app incorporates the device by this name when you adopt the [`EnergyKit LoadEvents Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.energykit.loadevents-experience).

## See Also

- [let deviceID: String](electrichvacloadevent/deviceid.md)
  The device’s unique stable identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electrichvacloadevent/devicename)*