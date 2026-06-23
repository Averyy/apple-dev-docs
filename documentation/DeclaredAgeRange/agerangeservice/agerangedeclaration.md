# AgeRangeService.AgeRangeDeclaration

**Framework**: Declared Age Range  
**Kind**: enum

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
- [AgeRangeService.AgeRangeDeclaration.selfDeclared](agerangeservice/agerangedeclaration/selfdeclared.md)
  Indicates the person signed in to iCloud to set their own age range.
- [AgeRangeService.AgeRangeDeclaration.guardianDeclared](agerangeservice/agerangedeclaration/guardiandeclared.md)
  Indicates a parent, guardian, or Family Organizer in a Family Sharing group set the age range.
- [AgeRangeService.AgeRangeDeclaration.confirmed](agerangeservice/agerangedeclaration/confirmed.md)
  Indicates a user’s age range was set using a scrutinized method, like a credit card or government ID.
### Deprecated
- [AgeRangeService.AgeRangeDeclaration.paymentChecked](agerangeservice/agerangedeclaration/paymentchecked.md)
  Indicates the person set their own age range using a payment method, like a credit card.
- [AgeRangeService.AgeRangeDeclaration.governmentIDChecked](agerangeservice/agerangedeclaration/governmentidchecked.md)
  Indicates the person set their own age range using a government ID.
- [AgeRangeService.AgeRangeDeclaration.checkedByOtherMethod](agerangeservice/agerangedeclaration/checkedbyothermethod.md)
  Indicates the person set their own age range using an unspecified method.
- [AgeRangeService.AgeRangeDeclaration.guardianPaymentChecked](agerangeservice/agerangedeclaration/guardianpaymentchecked.md)
  Indicates a parent, guardian, or Family Organizer in a Family Sharing group set the age range using a payment method, like a credit card.
- [AgeRangeService.AgeRangeDeclaration.guardianGovernmentIDChecked](agerangeservice/agerangedeclaration/guardiangovernmentidchecked.md)
  Indicates a parent, guardian, or Family Organizer in a Family Sharing group set the age range using a government ID.
- [AgeRangeService.AgeRangeDeclaration.guardianCheckedByOtherMethod](agerangeservice/agerangedeclaration/guardiancheckedbyothermethod.md)
  Indicates a parent, guardian, or Family Organizer in a Family Sharing group set the age range using an unspecified method.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [AgeRangeService.AgeRange](agerangeservice/agerange.md)
  Information about a person’s age range based on their response to your age range request.
- [func requestAgeRange(ageGates: Int, Int?, Int?, in: UIViewController) async throws -> AgeRangeService.Response](agerangeservice/requestagerange(agegates:_:_:in:)-2go8c.md)
  Requests an age range for the person signed in to iCloud on the device.
- [func requestAgeRange(ageGates: Int, Int?, Int?, in: NSWindow) async throws -> AgeRangeService.Response](agerangeservice/requestagerange(agegates:_:_:in:)-4yo3r.md)
  Requests an age range for the person logged onto iCloud on the device.
- [AgeRangeService.Response](agerangeservice/response.md)
  A response indicating whether a person shared their age range or declined to share it.
- [AgeRangeService.ParentalControls](agerangeservice/parentalcontrols.md)
  An option set to define parental controls enabled and shared as a part of age range declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/agerangedeclaration)*