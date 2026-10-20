# AgeRangeService.AgeRangeDeclaration

**Framework**: Declared Age Range  
**Kind**: enum  
**Role**: Enumeration

Constants that describe how an adult, parent, or guardian set the age range.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
enum AgeRangeDeclaration
```

#### Overview

The system provides this information to help you understand the reliability and source of the age range data. Different declaration types may be appropriate for different types of content experiences in your app.

## Topics

### Determining the age set method
- [AgeRangeService.AgeRangeDeclaration.selfDeclared](./agerangedeclaration/selfdeclared.md)
  Indicates the person signed in to iCloud to set their own age range.
- [AgeRangeService.AgeRangeDeclaration.guardianDeclared](./agerangedeclaration/guardiandeclared.md)
  Indicates a parent, guardian, or Family Organizer in a Family Sharing group set the age range.
- [AgeRangeService.AgeRangeDeclaration.confirmed](./agerangedeclaration/confirmed.md)
  A status that indicates a person confirmed their age-range declaration using a credit card or government ID.
### Deprecated
- [AgeRangeService.AgeRangeDeclaration.paymentChecked](./agerangedeclaration/paymentchecked.md)
  Indicates the person set their own age range using a payment method, like a credit card.
- [AgeRangeService.AgeRangeDeclaration.governmentIDChecked](./agerangedeclaration/governmentidchecked.md)
  Indicates the person set their own age range using a government ID.
- [AgeRangeService.AgeRangeDeclaration.checkedByOtherMethod](./agerangedeclaration/checkedbyothermethod.md)
  Indicates the person set their own age range using an unspecified method.
- [AgeRangeService.AgeRangeDeclaration.guardianPaymentChecked](./agerangedeclaration/guardianpaymentchecked.md)
  Indicates a parent, guardian, or Family Organizer in a Family Sharing group set the age range using a payment method, like a credit card.
- [AgeRangeService.AgeRangeDeclaration.guardianGovernmentIDChecked](./agerangedeclaration/guardiangovernmentidchecked.md)
  Indicates a parent, guardian, or Family Organizer in a Family Sharing group set the age range using a government ID.
- [AgeRangeService.AgeRangeDeclaration.guardianCheckedByOtherMethod](./agerangedeclaration/guardiancheckedbyothermethod.md)
  Indicates a parent, guardian, or Family Organizer in a Family Sharing group set the age range using an unspecified method.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the age range
- [AgeRangeService.AgeRange](./agerange.md)
  Information about a person’s age range based on their response to an age range request.
- [func requestAgeRange(ageGates: Int, Int?, Int?, in: UIViewController) async throws -> AgeRangeService.Response](./requestagerange%28agegates,_,_,in%29-2go8c.md)
  Requests an age range for the person signed in to iCloud on the device.
- [func requestAgeRange(ageGates: Int, Int?, Int?, in: NSWindow) async throws -> AgeRangeService.Response](./requestagerange%28agegates,_,_,in%29-4yo3r.md)
  Requests an age range for the person logged onto iCloud on the device.
- [AgeRangeService.Response](./response.md)
  A response indicating whether a person shared their age range or declined to share it.
- [AgeRangeService.ParentalControls](./parentalcontrols.md)
  An option set to define parental controls enabled and shared as a part of age range declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/agerangedeclaration)*