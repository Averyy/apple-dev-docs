# ASImportableCredential.PersonName

**Framework**: Authentication Services  
**Kind**: struct  
**Role**: Structure

A representation of PersonName as defined in the [Credential Exchange Format (CXF) specs](https://fidoalliance.org/specs/cx/cxf-v1.0-rd-20250313.html) This represents a person’s name.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct PersonName
```

## Topics

### Initializers
- [init(title: ASImportableEditableField?, given: ASImportableEditableField?, givenInformal: ASImportableEditableField?, given2: ASImportableEditableField?, surnamePrefix: ASImportableEditableField?, surname: ASImportableEditableField?, surname2: ASImportableEditableField?, credentials: ASImportableEditableField?, generation: ASImportableEditableField?)](./personname/init%28title,given,giveninformal,given2,surnameprefix,surname,surname2,credentials,generation%29.md)
### Instance Properties
- [var credentials: ASImportableEditableField?](./personname/credentials.md)
- [var generation: ASImportableEditableField?](./personname/generation.md)
- [var given: ASImportableEditableField?](./personname/given.md)
- [var given2: ASImportableEditableField?](./personname/given2.md)
- [var givenInformal: ASImportableEditableField?](./personname/giveninformal.md)
- [var surname: ASImportableEditableField?](./personname/surname.md)
- [var surname2: ASImportableEditableField?](./personname/surname2.md)
- [var surnamePrefix: ASImportableEditableField?](./personname/surnameprefix.md)
- [var title: ASImportableEditableField?](./personname/title.md)

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportablecredential/personname)*