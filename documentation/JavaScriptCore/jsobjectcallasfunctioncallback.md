# JSObjectCallAsFunctionCallback

**Framework**: JavaScriptCore  
**Kind**: typealias

The callback type for calling an object as a function.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
typealias JSObjectCallAsFunctionCallback = (JSContextRef?, JSObjectRef?, JSObjectRef?, Int, UnsafePointer<JSValueRef?>?, UnsafeMutablePointer<JSValueRef?>?) -> JSValueRef?
```

#### Return Value

A [`JSValueRef`](jsvalueref.md) that is the function’s return value.

#### Discussion

If you name your function `CallAsFunction`, you declare it like this:

```c
JSValueRef CallAsFunction(JSContextRef ctx, JSObjectRef function, JSObjectRef thisObject, size_t argumentCount, const JSValueRef arguments[], JSValueRef* exception);
```

If the JavaScript expression `myObject.myFunction()` invokes your callback, it sets `function` to `myFunction`, and `thisObject` to `myObject`.

If this callback is `NULL`, calling your object as a function throws an exception.

## Parameters

- `ctx`: The execution context to use.
- `function`: A   that is the function to call.
- `thisObject`: A   that is the   variable in the function’s scope.
- `argumentCount`: An integer count of the number of arguments in  .
- `arguments`: A   array of the arguments to pass to the function.
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
- [typealias JSObjectDeletePropertyCallback](jsobjectdeletepropertycallback.md)
  The callback type for deleting a property.
- [var getPropertyNames: JSObjectGetPropertyNamesCallback!](jsclassdefinition/getpropertynames.md)
  The callback for collecting the names of an object’s properties.
- [typealias JSObjectGetPropertyNamesCallback](jsobjectgetpropertynamescallback.md)
  The callback type for collecting the names of an object’s properties.
- [var callAsFunction: JSObjectCallAsFunctionCallback!](jsclassdefinition/callasfunction.md)
  The callback for calling an object as a function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsobjectcallasfunctioncallback)*