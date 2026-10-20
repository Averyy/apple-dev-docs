# className

**Framework**: JavaScriptCore  
**Kind**: property  
**Role**: Instance Property

A null-terminated UTF-8 string that contains the class’s name.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var className: UnsafePointer<CChar>!
```

```c
const char * className;
```

## See Also

### Managing Class Information
- [var parentClass: JSClassRef!](./parentclass.md)
  A JavaScript class to set as the class’s parent class.
- [var version: Int32](./version.md)
  The version of the class definition structure.
- [var attributes: JSClassAttributes](./attributes.md)
  A set of class attributes to give to the class.
- [var staticValues: UnsafePointer<JSStaticValue>!](./staticvalues.md)
  An array that contains the class’s statically declared value properties.
- [struct JSStaticValue](../jsstaticvalue.md)
  A statically declared value property.
- [var staticFunctions: UnsafePointer<JSStaticFunction>!](./staticfunctions.md)
  An array that contains the class’s statically declared function properties.
- [struct JSStaticFunction](../jsstaticfunction.md)
  A statically declared function property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsclassdefinition/classname)*