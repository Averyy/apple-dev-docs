# CMIOExtensionPropertyState

**Framework**: Core Media I/O  
**Kind**: class

An object that describes the state of a property.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
class CMIOExtensionPropertyState<ObjectType> where ObjectType : AnyObject
```

#### Overview

Create a property state object by specifying the type of data it stores, which must be a [`NSString`](https://developer.apple.com/documentation/foundation/nsstring), [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber), [`NSDictionary`](https://developer.apple.com/documentation/foundation/nsdictionary), [`NSArray`](https://developer.apple.com/documentation/foundation/nsarray), or [`NSData`](https://developer.apple.com/documentation/foundation/nsdata). You can optionally specify attributes that restrict the range of values a property allows.

## Topics

### Creating a Property State
- [convenience init(value: ObjectType?)](cmioextensionpropertystate/init(value:).md)
  Creates a property state with a value.
- [init(value: ObjectType?, attributes: CMIOExtensionPropertyAttributes<ObjectType>?)](cmioextensionpropertystate/init(value:attributes:).md)
  Creates a property state with a value and attributes.
### Inspecting a Property State
- [var value: ObjectType?](cmioextensionpropertystate/value.md)
  The value for a property state.
- [var attributes: CMIOExtensionPropertyAttributes<ObjectType>?](cmioextensionpropertystate/attributes.md)
  The attributes for a property state.
### Initializers
- [init?(coder: NSCoder)](cmioextensionpropertystate/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [struct CMIOExtensionProperty](cmioextensionproperty.md)
  A structure that defines the properties that providers, devices, and streams support.
- [class CMIOExtensionPropertyAttributes](cmioextensionpropertyattributes.md)
  An object that describes the attributes of a property.
- [let CMIOExtensionInfoDictionaryKey: String](cmioextensioninfodictionarykey.md)
  A key that specifies the extension information dictionary.
- [let CMIOExtensionMachServiceNameKey: String](cmioextensionmachservicenamekey.md)
  A key that specifies the mach service name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionpropertystate)*