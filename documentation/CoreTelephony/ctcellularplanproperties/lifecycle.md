# CTCellularPlanProperties.lifecycle

**Framework**: Core Telephony  
**Kind**: class  
**Role**: Class

A type that contains lifecycle details for a time-limited cellular plan.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
class lifecycle
```

```objc
@interface CTCellularPlanLifecycleProperties : NSObject
```

## Overview

This type contains lifecycle details for a time-limited cellular plan, including information such as when the plan expires. The expiration date determines the installation experience and when the system deactivates the plan.

## Topics

### Specifying the expiration date
- [var expirationDate: DateComponents](./lifecycle/expirationdate.md)
  The date when the time-limited cellular plan expires, specified with day-level granularity.
### Initializers
- [init?(coder: NSCoder)](./lifecycle/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCoding](../../Foundation/nscoding.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../../Foundation/nssecurecoding.md)

## See Also

### Getting the eSIM properties
- [var associatedIccid: String?](./associatediccid.md)
  The integrated circuit card identifier (ICCID) that identifies a SIM.
- [var simCapability: CTCellularPlanCapability](./simcapability.md)
  The available type of cellular plan that your eSIM supports.
- [var supportedRegionCodes: [Locale.Region]](./supportedregioncodes-yhu5.md)
  The available regions that your eSIM supports.
- [var lifecycleProperties: CTCellularPlanProperties.lifecycle?](./lifecycleproperties.md)
  The lifecycle details for a time-limited cellular plan.
- [supportedRegionCodes](./supportedregioncodes-5elox.md)
  The available regions that your eSIM supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanproperties/lifecycle)*