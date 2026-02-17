# expirationDate

**Framework**: Core Telephony  
**Kind**: property

The date when the time-limited cellular plan expires, specified with day-level granularity.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var expirationDate: DateComponents { get set }
```

#### Overview

The expiration date determines the installation experience and lifecycle behavior of the cellular plan. Specify the expiration date using day-level granularity (for example, February 1st, 2025) rather than including time components (for example, February 1st, 2025 12:30:35 PM).

The expiration date determines the following behavior:

- : If the expiration date falls within three calendar days from the current date (for example, January 3rd to January 6th), the system sets the eSIM as the default data line upon installation and skips the SIM setup flow when the device enters dual-SIM mode. The system also automatically labels the eSIM with the carrier name. For devices in single-SIM mode, the system sets the eSIM as the default data line and labels it with the carrier name.
- : If the expiration date falls more than three calendar days away (for example, January 7th or later when the current date is January 3rd), the eSIM installs normally and the person proceeds through the standard SIM setup flow.
- : For both scenarios above, the system automatically deactivates the eSIM at 5 AM on the expiration date.
- : If the expiration date exceeds forty-five days from the current date, or if the expiration date is invalid, the system rejects the installation and the operation fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanproperties/lifecycle/expirationdate)*