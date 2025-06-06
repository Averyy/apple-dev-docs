# JSClassDefinition

**Framework**: JavaScriptCore  
**Kind**: struct

A structure that contains properties and callbacks that define a type of object.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct JSClassDefinition
```

#### Overview

All fields other than the [`version`](jsclassdefinition/version.md) field are optional. Any pointer may be `NULL`.

The [`staticValues`](jsclassdefinition/staticvalues.md) and [`staticFunctions`](jsclassdefinition/staticfunctions.md) arrays are the simplest and most efficient means for vending custom properties. Statically declared properties automatically service requests like [`getProperty`](jsclassdefinition/getproperty.md), [`setProperty`](jsclassdefinition/setproperty.md), and [`getPropertyNames`](jsclassdefinition/getpropertynames.md). Property access callbacks are necessary only to implement unusual properties, like array indexes, which have unknown names at compile time.

If you name your getter function `GetX` and your setter function `SetX`, you declare a [`JSStaticValue`](jsstaticvalue.md) array that contains `"X"` like this:

```c
JSStaticValue StaticValueArray[] = { 
    { "X", GetX, SetX, kJSPropertyAttributeNone }, 
    { 0, 0, 0, 0 } 
};
```

Standard JavaScript practice calls for storing function objects in prototypes so you can share them. The default [`JSClassRef`](jsclassref.md) that [`JSClassCreate(_:)`](jsclasscreate(_:).md) creates follows this idiom, instantiating objects with a shared, automatically generating prototype that contains the class’s function objects. The [`kJSClassAttributeNoAutomaticPrototype`](kjsclassattributenoautomaticprototype.md) attribute specifies that a [`JSClassRef`](jsclassref.md) doesn’t automatically generate such a prototype. The resulting [`JSClassRef`](jsclassref.md) instantiates objects with the default object prototype, and gives each instance object its own copy of the class’s function objects.

A `NULL` callback specifies that the default object callback substitutes, except in the case of [`hasProperty`](jsclassdefinition/hasproperty.md), where it specifies that [`getProperty`](jsclassdefinition/getproperty.md) substitutes.

## Topics

### Creating a Class Definition
- [init()](jsclassdefinition/init.md)
  Creates an empty class definition.
- [init(version: Int32, attributes: JSClassAttributes, className: UnsafePointer<CChar>!, parentClass: JSClassRef!, staticValues: UnsafePointer<JSStaticValue>!, staticFunctions: UnsafePointer<JSStaticFunction>!, initialize: JSObjectInitializeCallback!, finalize: JSObjectFinalizeCallback!, hasProperty: JSObjectHasPropertyCallback!, getProperty: JSObjectGetPropertyCallback!, setProperty: JSObjectSetPropertyCallback!, deleteProperty: JSObjectDeletePropertyCallback!, getPropertyNames: JSObjectGetPropertyNamesCallback!, callAsFunction: JSObjectCallAsFunctionCallback!, callAsConstructor: JSObjectCallAsConstructorCallback!, hasInstance: JSObjectHasInstanceCallback!, convertToType: JSObjectConvertToTypeCallback!)](jsclassdefinition/init(version:attributes:classname:parentclass:staticvalues:staticfunctions:initialize:finalize:hasproperty:getproperty:setproperty:deleteproperty:getpropertynames:callasfunction:callasconstructor:hasinstance:converttotype:).md)
  Creates a class definition with the specified values.
- [typealias JSClassAttributes](jsclassattributes.md)
  A set of JavaScript class attributes.
### Managing Class Information
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
- [struct JSStaticFunction](jsstaticfunction.md)
  A statically declared function property.
### Managing Callbacks
- [var initialize: JSObjectInitializeCallback!](jsclassdefinition/initialize.md)
  The callback for creating the object.
- [typealias JSObjectInitializeCallback](jsobjectinitializecallback.md)
  The callback type for first creating an object.
- [var finalize: JSObjectFinalizeCallback!](jsclassdefinition/finalize.md)
  The callback for preparing the object for garbage collection.
- [typealias JSObjectFinalizeCallback](jsobjectfinalizecallback.md)
  The callback type for finalizing an object (preparing it for garbage collection).
- [var hasProperty: JSObjectHasPropertyCallback!](jsclassdefinition/hasproperty.md)
  The callback for determining whether an object has a property.
- [typealias JSObjectHasPropertyCallback](jsobjecthaspropertycallback.md)
  The callback type for determining whether an object has a property.
- [var getProperty: JSObjectGetPropertyCallback!](jsclassdefinition/getproperty.md)
  The callback for getting a property’s value.
- [typealias JSObjectGetPropertyCallback](jsobjectgetpropertycallback.md)
  The callback type for getting a property’s value.
- [var setProperty: JSObjectSetPropertyCallback!](jsclassdefinition/setproperty.md)
  The callback for setting a property’s value.
- [typealias JSObjectSetPropertyCallback](jsobjectsetpropertycallback.md)
  The callback type for setting a property’s value.
- [var deleteProperty: JSObjectDeletePropertyCallback!](jsclassdefinition/deleteproperty.md)
  The callback for deleting a property.
- [typealias JSObjectDeletePropertyCallback](jsobjectdeletepropertycallback.md)
  The callback type for deleting a property.
- [var getPropertyNames: JSObjectGetPropertyNamesCallback!](jsclassdefinition/getpropertynames.md)
  The callback for collecting the names of an object’s properties.
- [typealias JSObjectGetPropertyNamesCallback](jsobjectgetpropertynamescallback.md)
  The callback type for collecting the names of an object’s properties.
- [var callAsFunction: JSObjectCallAsFunctionCallback!](jsclassdefinition/callasfunction.md)
  The callback for calling an object as a function.
- [typealias JSObjectCallAsFunctionCallback](jsobjectcallasfunctioncallback.md)
  The callback type for calling an object as a function.
- [var hasInstance: JSObjectHasInstanceCallback!](jsclassdefinition/hasinstance.md)
  The callback for checking whether an object is an instance of a particular type.
- [typealias JSObjectHasInstanceCallback](jsobjecthasinstancecallback.md)
  The callback type for checking whether an object is an instance of a particular type.
- [var callAsConstructor: JSObjectCallAsConstructorCallback!](jsclassdefinition/callasconstructor.md)
  The callback for using an object as a constructor.
- [typealias JSObjectCallAsConstructorCallback](jsobjectcallasconstructorcallback.md)
  The callback type for using an object as a constructor.
- [var convertToType: JSObjectConvertToTypeCallback!](jsclassdefinition/converttotype.md)
  The callback for converting an object to a particular JavaScript type.
- [typealias JSObjectConvertToTypeCallback](jsobjectconverttotypecallback.md)
  The callback type for converting an object to a particular JavaScript type.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [func JSClassCreate(UnsafePointer<JSClassDefinition>!) -> JSClassRef!](jsclasscreate(_:).md)
  Creates a JavaScript class.
- [func JSClassRelease(JSClassRef!)](jsclassrelease(_:).md)
  Releases a JavaScript class.
- [func JSClassRetain(JSClassRef!) -> JSClassRef!](jsclassretain(_:).md)
  Retains a JavaScript class.
- [let kJSClassDefinitionEmpty: JSClassDefinition](kjsclassdefinitionempty.md)
  A class definition structure of the current version that contains null pointers and has no attributes.
- [JSClassAttribute](jsclassattribute.md)
  A JavaScript class attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsclassdefinition)*