# AppleCareCoverage.Attributes

**Framework**: AppleSchoolManagerAPI  
**Kind**: dictionary  
**Role**: Object

Attributes for an organization device’s AppleCare coverage resource.

**Availability**:
- Apple School Manager API 1.8+

## Declaration

```
object AppleCareCoverage.Attributes
```

## Overview

> **Note**: When additional attributes are added by Apple, they appear automatically, without requiring a newer version of the API.

#### Status

| **Possible values** | **Description** |
| --- | --- |
| `ACTIVE` | Coverage is currently active. |
| `INACTIVE` | Coverage is currently inactive. |

#### PaymentType

| **Possible values** | **Description** |
| --- | --- |
| `ABE_SUBSCRIPTION` | AppleCare+ for Business. |
| `PAID_UP_FRONT` | Coverage was paid in full at time of purchase. |
| `SUBSCRIPTION` | Coverage has recurring billing. |
| `NONE` | No payment type is associated with coverage (for example, Limited Warranty Coverage). |

## Properties

- `status` (AppleCareCoverageStatus): The current status of device coverage. Possible values: ‘ACTIVE’, ‘INACTIVE’
- `paymentType` (AppleCareCoveragePaymentType): Payment type of device coverage. Possible values: ‘ABE_SUBSCRIPTION’, ‘PAID_UP_FRONT’, ‘SUBSCRIPTION’, ‘NONE’
- `description` (string): Description of device coverage.
- `startDateTime` (date-time): UTC date when coverage period commenced. For AppleCare+ for Business, it’s UTC date when a device enrolls into the plan.
- `endDateTime` (date-time): UTC date when coverage period ends for the device. This field isn’t applicable for AppleCare+ for Business.
- `isRenewable` (boolean): Indicates whether coverage renews after endDateTime for the device. This field isn’t applicable for Limited Warranty.
- `isCanceled` (boolean): Indicates whether coverage is canceled for the device. This field isn’t applicable for Limited Warranty and AppleCare+ for Business.
- `contractCancelDateTime` (date-time): UTC date when coverage was canceled for the device. This field isn’t applicable for Limited Warranty and AppleCare+ for Business.
- `agreementNumber` (string): Agreement number associated with device coverage. This field isn’t applicable for Limited Warranty and AppleCare+ for Business.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appleschoolmanagerapi/applecarecoverage/attributes-data.dictionary)*