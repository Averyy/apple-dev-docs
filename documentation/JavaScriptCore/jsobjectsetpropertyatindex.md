# JSObjectSetPropertyAtIndex(_:_:_:_:_:)

**Framework**: JavaScriptCore  
**Kind**: func

Sets a property on an object by numeric index.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSObjectSetPropertyAtIndex(_ ctx: JSContextRef!, _ object: JSObjectRef!, _ propertyIndex: UInt32, _ value: JSValueRef!, _ exception: UnsafeMutablePointer<JSValueRef?>!)
```

#### Discussion

Calling [`JSObjectSetPropertyAtIndex(_:_:_:_:_:)`](jsobjectsetpropertyatindex(_:_:_:_:_:).md) is equivalent to calling [`JSObjectSetProperty(_:_:_:_:_:_:)`](jsobjectsetproperty(_:_:_:_:_:_:).md) with a string that contain `propertyIndex`, but [`JSObjectSetPropertyAtIndex(_:_:_:_:_:)`](jsobjectsetpropertyatindex(_:_:_:_:_:).md) provides optimized access to numeric properties.

## Parameters

- `ctx`: The execution context to use.
- `object`: The   with the property you want to set.
- `propertyIndex`: The property’s name as a number.
- `value`: A   to use as the property’s value.
- `exception`: A pointer to a   to store an exception in, if any. Pass   to discard any exception.

## See Also

- [func JSObjectCallAsConstructor(JSContextRef!, JSObjectRef!, Int, UnsafePointer<JSValueRef?>!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](jsobjectcallasconstructor(_:_:_:_:_:).md)
  Calls an object as a constructor.
- [func JSObjectCallAsFunction(JSContextRef!, JSObjectRef!, JSObjectRef!, Int, UnsafePointer<JSValueRef?>!, UnsafeMutablePointer<JSValueRef?>!) -> JSValueRef!](jsobjectcallasfunction(_:_:_:_:_:_:).md)
  Calls an object as a function.
- [func JSObjectCopyPropertyNames(JSContextRef!, JSObjectRef!) -> JSPropertyNameArrayRef!](jsobjectcopypropertynames(_:_:).md)
  Gets the names of an object’s enumerable properties.
- [func JSObjectDeleteProperty(JSContextRef!, JSObjectRef!, JSStringRef!, UnsafeMutablePointer<JSValueRef?>!) -> Bool](jsobjectdeleteproperty(_:_:_:_:).md)
  Deletes a property from an object.
- [func JSObjectGetPrivate(JSObjectRef!) -> UnsafeMutableRawPointer!](jsobjectgetprivate(_:).md)
  Gets an object’s private data.
- [func JSObjectGetProperty(JSContextRef!, JSObjectRef!, JSStringRef!, UnsafeMutablePointer<JSValueRef?>!) -> JSValueRef!](jsobjectgetproperty(_:_:_:_:).md)
  Gets a property from an object.
- [func JSObjectGetPropertyAtIndex(JSContextRef!, JSObjectRef!, UInt32, UnsafeMutablePointer<JSValueRef?>!) -> JSValueRef!](jsobjectgetpropertyatindex(_:_:_:_:).md)
  Gets a property from an object by numeric index.
- [func JSObjectGetPrototype(JSContextRef!, JSObjectRef!) -> JSValueRef!](jsobjectgetprototype(_:_:).md)
  Gets an object’s prototype.
- [func JSObjectHasProperty(JSContextRef!, JSObjectRef!, JSStringRef!) -> Bool](jsobjecthasproperty(_:_:_:).md)
  Tests whether an object has a specified property.
- [func JSObjectIsConstructor(JSContextRef!, JSObjectRef!) -> Bool](jsobjectisconstructor(_:_:).md)
  Tests whether you can call an object as a constructor.
- [func JSObjectIsFunction(JSContextRef!, JSObjectRef!) -> Bool](jsobjectisfunction(_:_:).md)
  Tests whether you can call an object as a function.
- [func JSObjectMake(JSContextRef!, JSClassRef!, UnsafeMutableRawPointer!) -> JSObjectRef!](jsobjectmake(_:_:_:).md)
  Creates a JavaScript object.
- [func JSObjectMakeArray(JSContextRef!, Int, UnsafePointer<JSValueRef?>!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](jsobjectmakearray(_:_:_:_:).md)
  Creates a JavaScript array object.
- [func JSObjectMakeConstructor(JSContextRef!, JSClassRef!, JSObjectCallAsConstructorCallback!) -> JSObjectRef!](jsobjectmakeconstructor(_:_:_:).md)
  Creates a JavaScript constructor.
- [func JSObjectMakeDate(JSContextRef!, Int, UnsafePointer<JSValueRef?>!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](jsobjectmakedate(_:_:_:_:).md)
  Creates a JavaScript date object as though invoking the built-in date constructor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsobjectsetpropertyatindex(_:_:_:_:_:))*