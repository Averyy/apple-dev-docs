# JSObjectIsFunction(_:_:)

**Framework**: JavaScriptCore  
**Kind**: func  
**Role**: Function

Tests whether you can call an object as a function.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSObjectIsFunction(_ ctx: JSContextRef!, _ object: JSObjectRef!) -> Bool
```

```c
bool JSObjectIsFunction(JSContextRef ctx, JSObjectRef object);
```

## Return Value

[`true`](../Swift/true.md) if you can call the object as a function; otherwise, [`false`](../Swift/false.md).

## Parameters

- `ctx`: The execution context to use.
- `object`: The [`JSObjectRef`](./jsobjectref.md) to test.

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
- [func JSObjectMake(JSContextRef!, JSClassRef!, UnsafeMutableRawPointer!) -> JSObjectRef!](./jsobjectmake%28_,_,_%29.md)
  Creates a JavaScript object.
- [func JSObjectMakeArray(JSContextRef!, Int, UnsafePointer<JSValueRef?>!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](./jsobjectmakearray%28_,_,_,_%29.md)
  Creates a JavaScript array object.
- [func JSObjectMakeConstructor(JSContextRef!, JSClassRef!, JSObjectCallAsConstructorCallback!) -> JSObjectRef!](./jsobjectmakeconstructor%28_,_,_%29.md)
  Creates a JavaScript constructor.
- [func JSObjectMakeDate(JSContextRef!, Int, UnsafePointer<JSValueRef?>!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](./jsobjectmakedate%28_,_,_,_%29.md)
  Creates a JavaScript date object as though invoking the built-in date constructor.
- [func JSObjectMakeError(JSContextRef!, Int, UnsafePointer<JSValueRef?>!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](./jsobjectmakeerror%28_,_,_,_%29.md)
  Creates a JavaScript error object as though invoking the built-in error constructor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsobjectisfunction(_:_:))*