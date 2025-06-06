# JSClassAttributes

**Framework**: JavaScriptCore  
**Kind**: typealias

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

#### Discussion

Combine multiple attributes by performing the logical OR operation.

## See Also

- [init()](jsclassdefinition/init.md)
  Creates an empty class definition.
- [init(version: Int32, attributes: JSClassAttributes, className: UnsafePointer<CChar>!, parentClass: JSClassRef!, staticValues: UnsafePointer<JSStaticValue>!, staticFunctions: UnsafePointer<JSStaticFunction>!, initialize: JSObjectInitializeCallback!, finalize: JSObjectFinalizeCallback!, hasProperty: JSObjectHasPropertyCallback!, getProperty: JSObjectGetPropertyCallback!, setProperty: JSObjectSetPropertyCallback!, deleteProperty: JSObjectDeletePropertyCallback!, getPropertyNames: JSObjectGetPropertyNamesCallback!, callAsFunction: JSObjectCallAsFunctionCallback!, callAsConstructor: JSObjectCallAsConstructorCallback!, hasInstance: JSObjectHasInstanceCallback!, convertToType: JSObjectConvertToTypeCallback!)](jsclassdefinition/init(version:attributes:classname:parentclass:staticvalues:staticfunctions:initialize:finalize:hasproperty:getproperty:setproperty:deleteproperty:getpropertynames:callasfunction:callasconstructor:hasinstance:converttotype:).md)
  Creates a class definition with the specified values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsclassattributes)*