# JSObjectSetPropertyForKey(_:_:_:_:_:_:)

**Framework**: JavaScriptCore  
**Kind**: func  
**Role**: Function

Sets a property on an object using a JavaScript value as the property key.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSObjectSetPropertyForKey(_ ctx: JSContextRef!, _ object: JSObjectRef!, _ propertyKey: JSValueRef!, _ value: JSValueRef!, _ attributes: JSPropertyAttributes, _ exception: UnsafeMutablePointer<JSValueRef?>!)
```

```c
void JSObjectSetPropertyForKey(JSContextRef ctx, JSObjectRef object, JSValueRef propertyKey, JSValueRef value, JSPropertyAttributes attributes, JSValueRef*exception);
```

## Discussion

This function is the same as performing `object[propertyKey] = value` from JavaScript.

## Parameters

- `ctx`: The execution context to use.
- `object`: The [`JSObjectRef`](./jsobjectref.md) with the property you want to set.
- `propertyKey`: A [`JSValueRef`](./jsvalueref.md) that contains the property key to use when looking up the property.
- `value`: A [`JSValueRef`](./jsvalueref.md) to use as the property’s value.
- `attributes`: A set of [`JSPropertyAttributes`](./jspropertyattributes.md) to give to the property.
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

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsobjectsetpropertyforkey(_:_:_:_:_:_:))*