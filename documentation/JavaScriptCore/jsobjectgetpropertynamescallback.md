# JSObjectGetPropertyNamesCallback

**Framework**: JavaScriptCore  
**Kind**: typealias

The callback type for collecting the names of an object’s properties.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
typealias JSObjectGetPropertyNamesCallback = (JSContextRef?, JSObjectRef?, JSPropertyNameAccumulatorRef?) -> Void
```

#### Discussion

If you name your function `GetPropertyNames`, you declare it like this:

```c
void GetPropertyNames(JSContextRef ctx, JSObjectRef object, JSPropertyNameAccumulatorRef propertyNames);
```

[`JSObjectCopyPropertyNames(_:_:)`](jsobjectcopypropertynames(_:_:).md) and JavaScript `for-in` loops use property name accumulators.

Use [`JSPropertyNameAccumulatorAddName(_:_:)`](jspropertynameaccumulatoraddname(_:_:).md) to add property names to `accumulator`. A class’s [`getPropertyNames`](jsclassdefinition/getpropertynames.md) callback only needs to provide the names of properties that the class vends through a custom [`getProperty`](jsclassdefinition/getproperty.md) or [`setProperty`](jsclassdefinition/setproperty.md) callback. The system adds other properties independently, including statically declared properties, properties that other classes vend, and properties that belong to the object’s prototype.

## Parameters

- `ctx`: The execution context to use.
- `object`: The   with the property names to collect.
- `accumulator`: A JavaScript property name accumulator to accumulate the names of the object’s properties in.

## See Also

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
- [var callAsFunction: JSObjectCallAsFunctionCallback!](jsclassdefinition/callasfunction.md)
  The callback for calling an object as a function.
- [typealias JSObjectCallAsFunctionCallback](jsobjectcallasfunctioncallback.md)
  The callback type for calling an object as a function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsobjectgetpropertynamescallback)*