# kABMultiStringPropertyType

**Framework**: Address Book  
**Kind**: var  
**Role**: Global Variable

Multistring property.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst

## Declaration

```swift
var kABMultiStringPropertyType: Int { get }
```

```c
kABMultiStringPropertyType
```

#### Discussion

Returned as an [`ABMultiValue`](./abmultivalue-swift.typealias.md) of [`CFString`](../CoreFoundation/cfstring.md) objects.

## See Also

### Constants
- [var kABInvalidPropertyType: Int](./kabinvalidpropertytype.md)
  Invalid property.
- [var kABStringPropertyType: Int](./kabstringpropertytype.md)
  String property. Returned as a [`CFString`](../CoreFoundation/cfstring.md) object.
- [var kABIntegerPropertyType: Int](./kabintegerpropertytype.md)
  Integer property. Returned as a [`CFNumber`](../CoreFoundation/cfnumber.md) object.
- [var kABRealPropertyType: Int](./kabrealpropertytype.md)
  Real property.
- [var kABDateTimePropertyType: Int](./kabdatetimepropertytype.md)
  Date-time property.
- [var kABDictionaryPropertyType: Int](./kabdictionarypropertytype.md)
  Dictionary property. Returned as a [`CFDictionary`](../CoreFoundation/cfdictionary.md) object.
- [var kABMultiIntegerPropertyType: Int](./kabmultiintegerpropertytype.md)
  Multiinteger property. Returned as an [`ABMultiValue`](./abmultivalue-swift.typealias.md) of [`CFNumber`](../CoreFoundation/cfnumber.md) objects.
- [var kABMultiRealPropertyType: Int](./kabmultirealpropertytype.md)
  Multireal property.
- [var kABMultiDateTimePropertyType: Int](./kabmultidatetimepropertytype.md)
  Multi–date-time property. Returned as an [`ABMultiValue`](./abmultivalue-swift.typealias.md) of [`CFDate`](../CoreFoundation/cfdate.md) objects.
- [var kABMultiDictionaryPropertyType: Int](./kabmultidictionarypropertytype.md)
  Multidictionary property. Returned as an [`ABMultiValue`](./abmultivalue-swift.typealias.md) of [`CFDictionary`](../CoreFoundation/cfdictionary.md) objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/kabmultistringpropertytype)*