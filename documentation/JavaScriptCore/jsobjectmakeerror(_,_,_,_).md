# JSObjectMakeError(_:_:_:_:)

**Framework**: JavaScriptCore  
**Kind**: func  
**Role**: Function

Creates a JavaScript error object as though invoking the built-in error constructor.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSObjectMakeError(_ ctx: JSContextRef!, _ argumentCount: Int, _ arguments: UnsafePointer<JSValueRef?>!, _ exception: UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!
```

```c
JSObjectRefJSObjectMakeError(JSContextRef ctx, size_t argumentCount, JSValueRef const arguments[], JSValueRef*exception);
```

## Return Value

A [`JSObjectRef`](./jsobjectref.md) that is an error.

## Parameters

- `ctx`: The execution context to use.
- `argumentCount`: An integer count of the number of arguments in `arguments`.
- `arguments`: A [`JSValueRef`](./jsvalueref.md) array of arguments to pass to the `Error` constructor. Pass `NULL` if `argumentCount` is `0`.
- `exception`: A pointer to a [`JSValueRef`](./jsvalueref.md) to store an exception in, if any. Pass `NULL` to discard any exception.

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
- [func JSObjectMake(JSContextRef!, JSClassRef!, UnsafeMutableRawPointer!) -> JSObjectRef!](./jsobjectmake%28_,_,_%29.md)
  Creates a JavaScript object.
- [func JSObjectMakeArray(JSContextRef!, Int, UnsafePointer<JSValueRef?>!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](./jsobjectmakearray%28_,_,_,_%29.md)
  Creates a JavaScript array object.
- [func JSObjectMakeConstructor(JSContextRef!, JSClassRef!, JSObjectCallAsConstructorCallback!) -> JSObjectRef!](./jsobjectmakeconstructor%28_,_,_%29.md)
  Creates a JavaScript constructor.
- [func JSObjectMakeDate(JSContextRef!, Int, UnsafePointer<JSValueRef?>!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](./jsobjectmakedate%28_,_,_,_%29.md)
  Creates a JavaScript date object as though invoking the built-in date constructor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsobjectmakeerror(_:_:_:_:))*