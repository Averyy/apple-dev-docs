# protocol_getProperty(_:_:_:_:)

**Framework**: Objective-C Runtime  
**Kind**: func

Returns the specified property of a given protocol.

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
func protocol_getProperty(_ proto: Protocol, _ name: UnsafePointer<CChar>, _ isRequiredProperty: Bool, _ isInstanceProperty: Bool) -> objc_property_t?
```

#### Return Value

The property specified by `name`, `isRequiredProperty`, and `isInstanceProperty` for `proto`, or `NULL` if none of `proto`’s properties meets the specification.

## Parameters

- `proto`: A protocol.
- `name`: The name of a property.
- `isRequiredProperty`: A Boolean value that indicates whether   is a required property.
- `isInstanceProperty`: A Boolean value that indicates whether   is an instance property.

## See Also

- [func objc_getProtocol(UnsafePointer<CChar>) -> Protocol?](objc_getprotocol(_:).md)
  Returns a specified protocol.
- [func objc_copyProtocolList(UnsafeMutablePointer<UInt32>?) -> AutoreleasingUnsafeMutablePointer<Protocol>?](objc_copyprotocollist(_:).md)
  Returns an array of all the protocols known to the runtime.
- [func objc_allocateProtocol(UnsafePointer<CChar>) -> Protocol?](objc_allocateprotocol(_:).md)
  Creates a new protocol instance.
- [func objc_registerProtocol(Protocol)](objc_registerprotocol(_:).md)
  Registers a newly created protocol with the Objective-C runtime.
- [func protocol_addMethodDescription(Protocol, Selector, UnsafePointer<CChar>?, Bool, Bool)](protocol_addmethoddescription(_:_:_:_:_:).md)
  Adds a method to a protocol.
- [func protocol_addProtocol(Protocol, Protocol)](protocol_addprotocol(_:_:).md)
  Adds a registered protocol to another protocol that is under construction.
- [func protocol_addProperty(Protocol, UnsafePointer<CChar>, UnsafePointer<objc_property_attribute_t>?, UInt32, Bool, Bool)](protocol_addproperty(_:_:_:_:_:_:).md)
  Adds a property to a protocol that is under construction.
- [func protocol_getName(Protocol) -> UnsafePointer<CChar>](protocol_getname(_:).md)
  Returns the name of a protocol.
- [func protocol_isEqual(Protocol?, Protocol?) -> Bool](protocol_isequal(_:_:).md)
  Returns a Boolean value that indicates whether two protocols are equal.
- [func protocol_copyMethodDescriptionList(Protocol, Bool, Bool, UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<objc_method_description>?](protocol_copymethoddescriptionlist(_:_:_:_:).md)
  Returns an array of method descriptions of methods meeting a given specification for a given protocol.
- [func protocol_getMethodDescription(Protocol, Selector, Bool, Bool) -> objc_method_description](protocol_getmethoddescription(_:_:_:_:).md)
  Returns a method description structure for a specified method of a given protocol.
- [func protocol_copyPropertyList(Protocol, UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<objc_property_t>?](protocol_copypropertylist(_:_:).md)
  Returns an array of the properties declared by a protocol.
- [func protocol_copyProtocolList(Protocol, UnsafeMutablePointer<UInt32>?) -> AutoreleasingUnsafeMutablePointer<Protocol>?](protocol_copyprotocollist(_:_:).md)
  Returns an array of the protocols adopted by a protocol.
- [func protocol_conformsToProtocol(Protocol?, Protocol?) -> Bool](protocol_conformstoprotocol(_:_:).md)
  Returns a Boolean value that indicates whether one protocol conforms to another protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/protocol_getproperty(_:_:_:_:))*