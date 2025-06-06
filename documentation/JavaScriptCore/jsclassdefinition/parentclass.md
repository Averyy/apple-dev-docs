# parentClass

**Framework**: JavaScriptCore  
**Kind**: property

A JavaScript class to set as the class’s parent class.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var parentClass: JSClassRef!
```

## See Also

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
- [struct JSStaticFunction](jsstaticfunction.md)
  A statically declared function property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsclassdefinition/parentclass)*