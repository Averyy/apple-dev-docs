# property_getName(_:)

**Framework**: Objective-C Runtime  
**Kind**: func  
**Role**: Function

Returns the name of a property.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func property_getName(_ property: objc_property_t) -> UnsafePointer<CChar>
```

```c
extern const char *property_getName(objc_property_t property);
```

## Return Value

A C string containing the property’s name.

## See Also

### Working with Properties
- [func property_getAttributes(objc_property_t) -> UnsafePointer<CChar>?](./property_getattributes%28_%29.md)
  Returns the attribute string of a property.
- [func property_copyAttributeValue(objc_property_t, UnsafePointer<CChar>) -> UnsafeMutablePointer<CChar>?](./property_copyattributevalue%28_,_%29.md)
  Returns the value of a property attribute given the attribute name.
- [func property_copyAttributeList(objc_property_t, UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<objc_property_attribute_t>?](./property_copyattributelist%28_,_%29.md)
  Returns an array of property attributes for a given property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/property_getname(_:))*