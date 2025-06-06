# JSStaticFunction

**Framework**: JavaScriptCore  
**Kind**: struct

A statically declared function property.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct JSStaticFunction
```

## Topics

### Creating a Static Function
- [init()](jsstaticfunction/init.md)
  Creates a static function.
- [init(name: UnsafePointer<CChar>!, callAsFunction: JSObjectCallAsFunctionCallback!, attributes: JSPropertyAttributes)](jsstaticfunction/init(name:callasfunction:attributes:).md)
  Creates a static function with the specified values.
### Accessing Static Function Information
- [var name: UnsafePointer<CChar>!](jsstaticfunction/name.md)
  A null-terminated UTF-8 string that contains the property’s name.
- [var callAsFunction: JSObjectCallAsFunctionCallback!](jsstaticfunction/callasfunction.md)
  A callback to invoke when calling the property as a function.
- [var attributes: JSPropertyAttributes](jsstaticfunction/attributes.md)
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
- [struct JSStaticValue](jsstaticvalue.md)
  A statically declared value property.
- [var staticFunctions: UnsafePointer<JSStaticFunction>!](jsclassdefinition/staticfunctions.md)
  An array that contains the class’s statically declared function properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsstaticfunction)*