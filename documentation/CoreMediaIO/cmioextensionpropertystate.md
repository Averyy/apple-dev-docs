# CMIOExtensionPropertyState

**Framework**: Core Media I/O  
**Kind**: class  
**Role**: Class

An object that describes the state of a property.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
class CMIOExtensionPropertyState<ObjectType> where ObjectType : AnyObject
```

```objc
@interface CMIOExtensionPropertyState : NSObject
```

#### Overview

Create a property state object by specifying the type of data it stores, which must be a [`NSString`](../Foundation/nsstring.md), [`NSNumber`](../Foundation/nsnumber.md), [`NSDictionary`](../Foundation/nsdictionary.md), [`NSArray`](../Foundation/nsarray.md), or [`NSData`](../Foundation/nsdata.md). You can optionally specify attributes that restrict the range of values a property allows.

## Topics

### Creating a Property State
- [convenience init(value: ObjectType?)](./cmioextensionpropertystate/init%28value%29.md)
  Creates a property state with a value.
- [init(value: ObjectType?, attributes: CMIOExtensionPropertyAttributes<ObjectType>?)](./cmioextensionpropertystate/init%28value,attributes%29.md)
  Creates a property state with a value and attributes.
- [+ propertyStateWithValue:](./cmioextensionpropertystate/propertystatewithvalue_.md)
  Returns a new property state with a value.
- [+ propertyStateWithValue:attributes:](./cmioextensionpropertystate/propertystatewithvalue_attributes_.md)
  Returns a new property state with a value and attributes.
### Inspecting a Property State
- [var value: ObjectType?](./cmioextensionpropertystate/value.md)
  The value for a property state.
- [var attributes: CMIOExtensionPropertyAttributes<ObjectType>?](./cmioextensionpropertystate/attributes.md)
  The attributes for a property state.
### Initializers
- [init?(coder: NSCoder)](./cmioextensionpropertystate/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Properties
- [struct CMIOExtensionProperty](./cmioextensionproperty.md)
  A structure that defines the properties that providers, devices, and streams support.
- [class CMIOExtensionPropertyAttributes](./cmioextensionpropertyattributes.md)
  An object that describes the attributes of a property.
- [let CMIOExtensionInfoDictionaryKey: String](./cmioextensioninfodictionarykey.md)
  A key that specifies the extension information dictionary.
- [let CMIOExtensionMachServiceNameKey: String](./cmioextensionmachservicenamekey.md)
  A key that specifies the mach service name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionpropertystate)*