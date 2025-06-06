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

Create a property state object by specifying the type of data it stores, which must be a [`NSString`](https://developer.apple.com/documentation/Foundation/NSString), [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber), [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary), [`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray), or [`NSData`](https://developer.apple.com/documentation/Foundation/NSData). You can optionally specify attributes that restrict the range of values a property allows.

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

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

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