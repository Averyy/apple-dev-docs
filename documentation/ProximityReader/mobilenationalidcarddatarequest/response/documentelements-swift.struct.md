# MobileNationalIDCardDataRequest.Response.DocumentElements

**Framework**: ProximityReader  
**Kind**: struct  
**Role**: Structure

A type that contains the document elements from a successful mobile national ID card data request.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
struct DocumentElements
```

## Topics

### Instance Properties
- [let age: Int?](./documentelements-swift.struct/age.md)
  The mobile national ID card holder’s age in years.
- [let ageAtLeastElements: [Int : Bool]](./documentelements-swift.struct/ageatleastelements.md)
  A dictionary of values that indicate whether the document holder is at least the specified age.
- [let dateOfBirth: DateComponents?](./documentelements-swift.struct/dateofbirth.md)
  The date of birth of the mobile national ID card holder.
- [let documentNumber: String?](./documentelements-swift.struct/documentnumber.md)
  The document’s number, as defined by the document’s issuing authority.
- [let name: MobileDocumentHolderName?](./documentelements-swift.struct/name.md)
  The mobile national ID card holder’s name.
- [var nameComponents: PersonNameComponents?](./documentelements-swift.struct/namecomponents.md)
  The mobile national ID card holder’s name components.
- [let portraitData: Data?](./documentelements-swift.struct/portraitdata.md)
  The portrait data of the mobile national ID card holder on record with the issuer.
- [let sex: MobileNationalIDCardDataRequest.Response.DocumentElements.Sex?](./documentelements-swift.struct/sex-swift.property.md)
  The mobile national ID card holder’s sex.
### Enumerations
- [MobileNationalIDCardDataRequest.Response.DocumentElements.Sex](./documentelements-swift.struct/sex-swift.enum.md)
  A type that represents the mobile national ID card holder’s sex.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobilenationalidcarddatarequest/response/documentelements-swift.struct)*