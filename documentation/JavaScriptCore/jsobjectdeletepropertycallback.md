# JSObjectDeletePropertyCallback

**Framework**: JavaScriptCore  
**Kind**: typealias

The callback type for deleting a property.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
typealias JSObjectDeletePropertyCallback = (JSContextRef?, JSObjectRef?, JSStringRef?, UnsafeMutablePointer<JSValueRef?>?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the deletion of `propertyName` succeeds; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

If you name your function `DeleteProperty`, you declare it like this:

```c
bool DeleteProperty(JSContextRef ctx, JSObjectRef object, JSStringRef propertyName, JSValueRef* exception);
```

If this function returns [`false`](https://developer.apple.com/documentation/Swift/false), the delete request forwards to the object’s statically declared properties, and then its parent class chain (which includes the default object class).

## Parameters

- `ctx`: The execution context to use.
- `object`: The   to delete the property in.
- `propertyName`: A   that contains the name of the property to delete.
- `exception`: A pointer to a   to return an exception in, if any.

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
- [var getPropertyNames: JSObjectGetPropertyNamesCallback!](jsclassdefinition/getpropertynames.md)
  The callback for collecting the names of an object’s properties.
- [typealias JSObjectGetPropertyNamesCallback](jsobjectgetpropertynamescallback.md)
  The callback type for collecting the names of an object’s properties.
- [var callAsFunction: JSObjectCallAsFunctionCallback!](jsclassdefinition/callasfunction.md)
  The callback for calling an object as a function.
- [typealias JSObjectCallAsFunctionCallback](jsobjectcallasfunctioncallback.md)
  The callback type for calling an object as a function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsobjectdeletepropertycallback)*