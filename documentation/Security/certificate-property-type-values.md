# Certificate Property Type Values

**Framework**: Security

Recognize the possible certificate property types.

#### Overview

These are the possible values that may be assigned to the [`kSecPropertyKeyType`](ksecpropertykeytype.md) key in each of the property dictionaries returned by a call to the [`SecCertificateCopyValues(_:_:_:)`](seccertificatecopyvalues(_:_:_:).md) function.

## Topics

### Constants
- [let kSecPropertyTypeWarning: CFString](ksecpropertytypewarning.md)
  A key whose value is a string describing a trust evaluation warning.
- [let kSecPropertyTypeSuccess: CFString](ksecpropertytypesuccess.md)
  A key whose value is a string describing a trust evaluation success.
- [let kSecPropertyTypeSection: CFString](ksecpropertytypesection.md)
  A key whose value is a string describing the name of a field in the certificate (`CFSTR("Subject Name")`, for example).
- [let kSecPropertyTypeData: CFString](ksecpropertytypedata.md)
  A key whose value is a data object.
- [let kSecPropertyTypeString: CFString](ksecpropertytypestring.md)
  A key whose value is a string.
- [let kSecPropertyTypeURL: CFString](ksecpropertytypeurl.md)
  Specifies a key whose value is a URL.
- [let kSecPropertyTypeDate: CFString](ksecpropertytypedate.md)
  Specifies a key whose value is a string containing a date (or a string listing the bytes of an invalid date).
- [let kSecPropertyTypeArray: CFString](ksecpropertytypearray.md)
  Specifies a key whose value is an array.
- [let kSecPropertyTypeNumber: CFString](ksecpropertytypenumber.md)
  Specifies a key whose value is a number.
- [let kSecPropertyTypeTitle: CFString](ksecpropertytypetitle.md)
  Specifies a key whose value is a string containing the title (display name) of the certificate.
- [let kSecPropertyTypeError: CFString](ksecpropertytypeerror.md)
  Specifies a key whose value is a string containing the reason for a trust evaluation failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/certificate-property-type-values)*