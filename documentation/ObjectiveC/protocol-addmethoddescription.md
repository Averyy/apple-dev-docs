# protocol_addMethodDescription(_:_:_:_:_:)

**Framework**: Objective-C Runtime  
**Kind**: func

Adds a method to a protocol.

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
func protocol_addMethodDescription(_ proto: Protocol, _ name: Selector, _ types: UnsafePointer<CChar>?, _ isRequiredMethod: Bool, _ isInstanceMethod: Bool)
```

#### Discussion

To add a method to a protocol using this function, the protocol must be under construction. That is, you must add any methods to `proto` before you register it with the Objective-C runtime (via the [`objc_registerProtocol(_:)`](objc_registerprotocol(_:).md) function).

## Parameters

- `proto`: The protocol you want to add a method to.
- `name`: The name of the method you want to add.
- `types`: A C string representing the signature of the method you want to add.
- `isRequiredMethod`: A Boolean indicating whether the method is a required method of the   protocol. If  , the method is a required method; if  , the method is an optional method.
- `isInstanceMethod`: A Boolean indicating whether the method is an instance method. If  , the method is an instance method; if  , the method is a class method.

## See Also

- [func objc_getProtocol(UnsafePointer<CChar>) -> Protocol?](objc_getprotocol(_:).md)
  Returns a specified protocol.
- [func objc_copyProtocolList(UnsafeMutablePointer<UInt32>?) -> AutoreleasingUnsafeMutablePointer<Protocol>?](objc_copyprotocollist(_:).md)
  Returns an array of all the protocols known to the runtime.
- [func objc_allocateProtocol(UnsafePointer<CChar>) -> Protocol?](objc_allocateprotocol(_:).md)
  Creates a new protocol instance.
- [func objc_registerProtocol(Protocol)](objc_registerprotocol(_:).md)
  Registers a newly created protocol with the Objective-C runtime.
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
- [func protocol_getProperty(Protocol, UnsafePointer<CChar>, Bool, Bool) -> objc_property_t?](protocol_getproperty(_:_:_:_:).md)
  Returns the specified property of a given protocol.
- [func protocol_copyProtocolList(Protocol, UnsafeMutablePointer<UInt32>?) -> AutoreleasingUnsafeMutablePointer<Protocol>?](protocol_copyprotocollist(_:_:).md)
  Returns an array of the protocols adopted by a protocol.
- [func protocol_conformsToProtocol(Protocol?, Protocol?) -> Bool](protocol_conformstoprotocol(_:_:).md)
  Returns a Boolean value that indicates whether one protocol conforms to another protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/protocol_addmethoddescription(_:_:_:_:_:))*