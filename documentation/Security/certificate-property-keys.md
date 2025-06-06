# Certificate Property Keys

**Framework**: Security

Recognize the dictionary keys that taken together define a certificate property.

#### Overview

These are the keys that appear in the property dictionaries that describe a certificate. Each property dictionary includes a key for the property type, a label for the property, a localized label, and the property value itself. Many property dictionaries are in turn collected into a larger dictionary that is returned by a call to the [`SecCertificateCopyValues(_:_:_:)`](seccertificatecopyvalues(_:_:_:).md) function.

## Topics

### Constants
- [let kSecPropertyKeyType: CFString](ksecpropertykeytype.md)
  A key whose value indicates the type of certificate property.
- [let kSecPropertyKeyLabel: CFString](ksecpropertykeylabel.md)
  A key whose value is the label for a certificate property.
- [let kSecPropertyKeyLocalizedLabel: CFString](ksecpropertykeylocalizedlabel.md)
  A key whose value is the localized label for a certificate property.
- [let kSecPropertyKeyValue: CFString](ksecpropertykeyvalue.md)
  A key whose value is the value for a certificate property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/certificate-property-keys)*