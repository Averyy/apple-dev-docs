# property_copyAttributeList(_:_:)

**Framework**: Objective-C Runtime  
**Kind**: func

Returns an array of property attributes for a given property.

**Availability**:
- iOS 4.3+
- iPadOS 4.3+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func property_copyAttributeList(_ property: objc_property_t, _ outCount: UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<objc_property_attribute_t>?
```

#### Return Value

An array of property attributes. You must free the array with `free()`.

## Parameters

- `property`: The property whose attributes you want to copy.
- `outCount`: The number of attributes returned in the array.

## See Also

- [func property_getName(objc_property_t) -> UnsafePointer<CChar>](property_getname(_:).md)
  Returns the name of a property.
- [func property_getAttributes(objc_property_t) -> UnsafePointer<CChar>?](property_getattributes(_:).md)
  Returns the attribute string of a property.
- [func property_copyAttributeValue(objc_property_t, UnsafePointer<CChar>) -> UnsafeMutablePointer<CChar>?](property_copyattributevalue(_:_:).md)
  Returns the value of a property attribute given the attribute name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/property_copyattributelist(_:_:))*