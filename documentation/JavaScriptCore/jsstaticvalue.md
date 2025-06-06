# JSStaticValue

**Framework**: JavaScriptCore  
**Kind**: struct

A statically declared value property.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct JSStaticValue
```

## Topics

### Creating a Static Value
- [init()](jsstaticvalue/init.md)
  Creates a static value.
- [init(name: UnsafePointer<CChar>!, getProperty: JSObjectGetPropertyCallback!, setProperty: JSObjectSetPropertyCallback!, attributes: JSPropertyAttributes)](jsstaticvalue/init(name:getproperty:setproperty:attributes:).md)
  Creates a static value with the specified values.
### Accessing Static Value Information
- [var name: UnsafePointer<CChar>!](jsstaticvalue/name.md)
  A null-terminated UTF-8 string that contains the property’s name.
- [var getProperty: JSObjectGetPropertyCallback!](jsstaticvalue/getproperty.md)
  A callback to invoke when getting the property’s value.
- [var setProperty: JSObjectSetPropertyCallback!](jsstaticvalue/setproperty.md)
  A callback to invoke when setting the property’s value.
- [var attributes: JSPropertyAttributes](jsstaticvalue/attributes.md)
  A set of property attributes to give to the property.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [var parentClass: JSClassRef!](jsclassdefinition/parentclass.md)
  A JavaScript class to set as the class’s parent class.
- [var className: UnsafePointer<CChar>!](jsclassdefinition/classname.md)
  A null-terminated UTF-8 string that contains the class’s name.
- [var version: Int32](jsclassdefinition/version.md)
  The version of the class definition structure.
- [var attributes: JSClassAttributes](jsclassdefinition/attributes.md)
  A set of class attributes to give to the class.
- [var staticValues: UnsafePointer<JSStaticValue>!](jsclassdefinition/staticvalues.md)
  An array that contains the class’s statically declared value properties.
- [var staticFunctions: UnsafePointer<JSStaticFunction>!](jsclassdefinition/staticfunctions.md)
  An array that contains the class’s statically declared function properties.
- [struct JSStaticFunction](jsstaticfunction.md)
  A statically declared function property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsstaticvalue)*