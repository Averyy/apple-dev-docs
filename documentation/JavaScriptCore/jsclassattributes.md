# JSClassAttributes

**Framework**: JavaScriptCore  
**Kind**: typealias  
**Role**: Type Alias

A set of JavaScript class attributes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
typealias JSClassAttributes = UInt32
```

```c
typedef unsigned int JSClassAttributes;
```

## Discussion

Combine multiple attributes by performing the logical OR operation.

## See Also

### Creating a Class Definition
- [init()](./jsclassdefinition/init%28%29.md)
  Creates an empty class definition.
- [init(version: Int32, attributes: JSClassAttributes, className: UnsafePointer<CChar>!, parentClass: JSClassRef!, staticValues: UnsafePointer<JSStaticValue>!, staticFunctions: UnsafePointer<JSStaticFunction>!, initialize: JSObjectInitializeCallback!, finalize: JSObjectFinalizeCallback!, hasProperty: JSObjectHasPropertyCallback!, getProperty: JSObjectGetPropertyCallback!, setProperty: JSObjectSetPropertyCallback!, deleteProperty: JSObjectDeletePropertyCallback!, getPropertyNames: JSObjectGetPropertyNamesCallback!, callAsFunction: JSObjectCallAsFunctionCallback!, callAsConstructor: JSObjectCallAsConstructorCallback!, hasInstance: JSObjectHasInstanceCallback!, convertToType: JSObjectConvertToTypeCallback!)](./jsclassdefinition/init%28version,attributes,classname,parentclass,staticvalues,staticfunctions,initialize,finalize,hasproperty,getproperty,setproperty,deleteproperty,getpropertynames,callasfunction,callasconstructor,hasinstance,converttotype%29.md)
  Creates a class definition with the specified values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsclassattributes)*