# JSObjectMake(_:_:_:)

**Framework**: JavaScriptCore  
**Kind**: func  
**Role**: Function

Creates a JavaScript object.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSObjectMake(_ ctx: JSContextRef!, _ jsClass: JSClassRef!, _ data: UnsafeMutableRawPointer!) -> JSObjectRef!
```

```c
JSObjectRefJSObjectMake(JSContextRef ctx, JSClassRef jsClass, void *data);
```

## Return Value

A [`JSObjectRef`](./jsobjectref.md) with the specified class and private data.

## Discussion

The default object class doesn’t allocate storage for private data, so you must provide a non-`NULL` `jsClass` to [`JSObjectMake(_:_:_:)`](./jsobjectmake%28_,_,_%29.md) if you want your object to be able to store private data.

The system sets `data` on the created object before calling the initialize methods in its class chain. This enables the initialize methods to retrieve and manipulate data through [`JSObjectGetPrivate(_:)`](./jsobjectgetprivate%28_%29.md).

## Parameters

- `ctx`: The execution context to use.
- `jsClass`: The [`JSClassRef`](./jsclassref.md) to assign to the object. Pass `NULL` to use the default object class.
- `data`: A pointer to set as the object’s private data. Pass `NULL` to specify no private data.

## See Also

### Working with Objects
- [func JSObjectCallAsConstructor(JSContextRef!, JSObjectRef!, Int, UnsafePointer<JSValueRef?>!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](./jsobjectcallasconstructor%28_,_,_,_,_%29.md)
  Calls an object as a constructor.
- [func JSObjectCallAsFunction(JSContextRef!, JSObjectRef!, JSObjectRef!, Int, UnsafePointer<JSValueRef?>!, UnsafeMutablePointer<JSValueRef?>!) -> JSValueRef!](./jsobjectcallasfunction%28_,_,_,_,_,_%29.md)
  Calls an object as a function.
- [func JSObjectCopyPropertyNames(JSContextRef!, JSObjectRef!) -> JSPropertyNameArrayRef!](./jsobjectcopypropertynames%28_,_%29.md)
  Gets the names of an object’s enumerable properties.
- [func JSObjectDeleteProperty(JSContextRef!, JSObjectRef!, JSStringRef!, UnsafeMutablePointer<JSValueRef?>!) -> Bool](./jsobjectdeleteproperty%28_,_,_,_%29.md)
  Deletes a property from an object.
- [func JSObjectGetPrivate(JSObjectRef!) -> UnsafeMutableRawPointer!](./jsobjectgetprivate%28_%29.md)
  Gets an object’s private data.
- [func JSObjectGetProperty(JSContextRef!, JSObjectRef!, JSStringRef!, UnsafeMutablePointer<JSValueRef?>!) -> JSValueRef!](./jsobjectgetproperty%28_,_,_,_%29.md)
  Gets a property from an object.
- [func JSObjectGetPropertyAtIndex(JSContextRef!, JSObjectRef!, UInt32, UnsafeMutablePointer<JSValueRef?>!) -> JSValueRef!](./jsobjectgetpropertyatindex%28_,_,_,_%29.md)
  Gets a property from an object by numeric index.
- [func JSObjectGetPrototype(JSContextRef!, JSObjectRef!) -> JSValueRef!](./jsobjectgetprototype%28_,_%29.md)
  Gets an object’s prototype.
- [func JSObjectHasProperty(JSContextRef!, JSObjectRef!, JSStringRef!) -> Bool](./jsobjecthasproperty%28_,_,_%29.md)
  Tests whether an object has a specified property.
- [func JSObjectIsConstructor(JSContextRef!, JSObjectRef!) -> Bool](./jsobjectisconstructor%28_,_%29.md)
  Tests whether you can call an object as a constructor.
- [func JSObjectIsFunction(JSContextRef!, JSObjectRef!) -> Bool](./jsobjectisfunction%28_,_%29.md)
  Tests whether you can call an object as a function.
- [func JSObjectMakeArray(JSContextRef!, Int, UnsafePointer<JSValueRef?>!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](./jsobjectmakearray%28_,_,_,_%29.md)
  Creates a JavaScript array object.
- [func JSObjectMakeConstructor(JSContextRef!, JSClassRef!, JSObjectCallAsConstructorCallback!) -> JSObjectRef!](./jsobjectmakeconstructor%28_,_,_%29.md)
  Creates a JavaScript constructor.
- [func JSObjectMakeDate(JSContextRef!, Int, UnsafePointer<JSValueRef?>!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](./jsobjectmakedate%28_,_,_,_%29.md)
  Creates a JavaScript date object as though invoking the built-in date constructor.
- [func JSObjectMakeError(JSContextRef!, Int, UnsafePointer<JSValueRef?>!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](./jsobjectmakeerror%28_,_,_,_%29.md)
  Creates a JavaScript error object as though invoking the built-in error constructor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsobjectmake(_:_:_:))*