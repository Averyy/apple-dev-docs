# property_copyAttributeValue(_:_:)

**Framework**: Objective-C Runtime  
**Kind**: func

Returns the value of a property attribute given the attribute name.

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
func property_copyAttributeValue(_ property: objc_property_t, _ attributeName: UnsafePointer<CChar>) -> UnsafeMutablePointer<CChar>?
```

#### Return Value

The value string of the `attributeName` attribute, if one exists in `property`; otherwise, `nil`. You must free the returned value string with `free()`.

## Parameters

- `property`: The property whose value you are interested in.
- `attributeName`: A C string representing the name of the attribute.

## See Also

- [func property_getName(objc_property_t) -> UnsafePointer<CChar>](property_getname(_:).md)
  Returns the name of a property.
- [func property_getAttributes(objc_property_t) -> UnsafePointer<CChar>?](property_getattributes(_:).md)
  Returns the attribute string of a property.
- [func property_copyAttributeList(objc_property_t, UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<objc_property_attribute_t>?](property_copyattributelist(_:_:).md)
  Returns an array of property attributes for a given property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/property_copyattributevalue(_:_:))*