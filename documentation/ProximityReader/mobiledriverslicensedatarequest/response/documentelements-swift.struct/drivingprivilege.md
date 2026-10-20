# MobileDriversLicenseDataRequest.Response.DocumentElements.DrivingPrivilege

**Framework**: ProximityReader  
**Kind**: struct  
**Role**: Structure

A type that represents a driving privilege which the mobile driver’s license holder possesses.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
struct DrivingPrivilege
```

## Topics

### Structures
- [MobileDriversLicenseDataRequest.Response.DocumentElements.DrivingPrivilege.Code](./drivingprivilege/code.md)
  An object representing a code of a driving privilege.
### Instance Properties
- [let codes: [MobileDriversLicenseDataRequest.Response.DocumentElements.DrivingPrivilege.Code]](./drivingprivilege/codes.md)
  The codes which describe the driving privilege.
- [let expirationDate: DateComponents?](./drivingprivilege/expirationdate.md)
  The expiration date of the driving privilege.
- [let issueDate: DateComponents?](./drivingprivilege/issuedate.md)
  The issue date of the driving privilege.
- [let vehicleCategoryCode: String](./drivingprivilege/vehiclecategorycode.md)
  The vehicle category code of the driving privilege.

## Relationships

### Conforms To
- [Equatable](../../../../Swift/equatable.md)
- [Hashable](../../../../Swift/hashable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledriverslicensedatarequest/response/documentelements-swift.struct/drivingprivilege)*