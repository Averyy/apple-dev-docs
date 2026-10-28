# CMIOExtensionPropertyAttributes

**Framework**: Core Media I/O  
**Kind**: class  
**Role**: Class

An object that describes the attributes of a property.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
class CMIOExtensionPropertyAttributes<ObjectType> where ObjectType : AnyObject
```

```objc
@interface CMIOExtensionPropertyAttributes : NSObject
```

## Overview

Use a property attributes object to describe attributes such as the minimum and maximum values, discrete values, and read-only values.

## Topics

### Creating Property Attributes
- [init(minValue: ObjectType?, maxValue: ObjectType?, validValues: [ObjectType]?, readOnly: Bool)](./cmioextensionpropertyattributes/init%28minvalue,maxvalue,validvalues,readonly%29.md)
  Creates a property attributes object with the specified configuration.
- [+ propertyAttributesWithMinValue:maxValue:validValues:readOnly:](./cmioextensionpropertyattributes/propertyattributeswithminvalue_maxvalue_validvalues_readonly_.md)
  Returns a new property attributes object with the specified configuration.
### Inspecting Attributes
- [var isReadOnly: Bool](./cmioextensionpropertyattributes/isreadonly.md)
  A Boolean value that indicates whether a property is read-only.
- [var minValue: ObjectType?](./cmioextensionpropertyattributes/minvalue.md)
  The minimum value a property supports.
- [var maxValue: ObjectType?](./cmioextensionpropertyattributes/maxvalue.md)
  The maximum value a property supports.
- [var validValues: [ObjectType]?](./cmioextensionpropertyattributes/validvalues.md)
  An array of discrete values that this property supports.
### Specifying a Read-Only Attribute
- [class var readOnlyPropertyAttribute: CMIOExtensionPropertyAttributes<AnyObject>](./cmioextensionpropertyattributes/readonlypropertyattribute.md)
  A class property for a read-only property attribute.
### Initializers
- [init?(coder: NSCoder)](./cmioextensionpropertyattributes/init%28coder%29.md)

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
- [class CMIOExtensionPropertyState](./cmioextensionpropertystate.md)
  An object that describes the state of a property.
- [let CMIOExtensionInfoDictionaryKey: String](./cmioextensioninfodictionarykey.md)
  A key that specifies the extension information dictionary.
- [let CMIOExtensionMachServiceNameKey: String](./cmioextensionmachservicenamekey.md)
  A key that specifies the mach service name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionpropertyattributes)*