# ABPropertyType

**Framework**: Address Book  
**Kind**: typealias

These are the possible types of ABRecord properties.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
typealias ABPropertyType = CFIndex
```

## Topics

### Constants
- [var kABErrorInProperty: _ABPropertyType](kaberrorinproperty.md)
  An invalid property was used.
- [var kABStringProperty: _ABPropertyType](kabstringproperty.md)
  This property is an `NSString` object.
- [var kABIntegerProperty: _ABPropertyType](kabintegerproperty.md)
  This property is an `NSNumber` object representing an integer.
- [var kABRealProperty: _ABPropertyType](kabrealproperty.md)
  This property is an `NSNumber` object representing a real number.
- [var kABDateProperty: _ABPropertyType](kabdateproperty.md)
  This property is an `NSDate` object.
- [var kABArrayProperty: _ABPropertyType](kabarrayproperty.md)
  This property is an `NSArray` object.
- [var kABDictionaryProperty: _ABPropertyType](kabdictionaryproperty.md)
  This property is an `NSDictionary` object.
- [var kABDataProperty: _ABPropertyType](kabdataproperty.md)
  This property is an `NSData` object.
- [var kABMultiStringProperty: _ABPropertyType](kabmultistringproperty.md)
  This property is an `ABMultiValue` object containing `NSString` objects.
- [var kABMultiIntegerProperty: _ABPropertyType](kabmultiintegerproperty.md)
  This property is an `ABMultiValue` object containing `NSNumber` objects representing integers.
- [var kABMultiRealProperty: _ABPropertyType](kabmultirealproperty.md)
  This property is an `ABMultiValue` object containing `NSNumber` objects representing real numbers.
- [var kABMultiDateProperty: _ABPropertyType](kabmultidateproperty.md)
  This property is an `ABMultiValue` object containing `NSDate` objects.
- [var kABMultiArrayProperty: _ABPropertyType](kabmultiarrayproperty.md)
  This property is an `ABMultiValue` object containing `NSArray` objects.
- [var kABMultiDictionaryProperty: _ABPropertyType](kabmultidictionaryproperty.md)
  This property is an `ABMultiValue` object containing `NSDictionary` objects.
- [var kABMultiDataProperty: _ABPropertyType](kabmultidataproperty.md)
  This property is an `ABMultiValue` object containing `NSData` objects.

## See Also

- [typealias ABSearchComparison](absearchcomparison.md)
  Constants used to specify the type of comparison beingmade.
- [typealias ABSearchConjunction](absearchconjunction.md)
  Constants used to create compound search elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpropertytype)*