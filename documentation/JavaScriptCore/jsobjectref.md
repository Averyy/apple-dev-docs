# JSObjectRef

**Framework**: JavaScriptCore  
**Kind**: typealias

A JavaScript object.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
typealias JSObjectRef = OpaquePointer
```

#### Discussion

A [`JSObjectRef`](jsobjectref.md) is a [`JSValueRef`](jsvalueref.md).

## Topics

### Accessing the Global Object
- [func JSContextGetGlobalObject(JSContextRef!) -> JSObjectRef!](jscontextgetglobalobject(_:).md)
  Gets the global object of a JavaScript execution context.
### Working with Objects
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
- [func JSObjectMakeError(JSContextRef!, Int, UnsafePointer<JSValueRef?>!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](jsobjectmakeerror(_:_:_:_:).md)
  Creates a JavaScript error object as though invoking the built-in error constructor.
- [func JSObjectMakeFunction(JSContextRef!, JSStringRef!, UInt32, UnsafePointer<JSStringRef?>!, JSStringRef!, JSStringRef!, Int32, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](jsobjectmakefunction(_:_:_:_:_:_:_:_:).md)
  Creates a function with a specified script as its body.
- [func JSObjectMakeFunctionWithCallback(JSContextRef!, JSStringRef!, JSObjectCallAsFunctionCallback!) -> JSObjectRef!](jsobjectmakefunctionwithcallback(_:_:_:).md)
  Creates a JavaScript function with a specified callback as its implementation.
- [func JSObjectMakeRegExp(JSContextRef!, Int, UnsafePointer<JSValueRef?>!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](jsobjectmakeregexp(_:_:_:_:).md)
  Creates a JavaScript regular expression object as though invoking the built-in regular expression constructor.
- [func JSObjectSetPrivate(JSObjectRef!, UnsafeMutableRawPointer!) -> Bool](jsobjectsetprivate(_:_:).md)
  Sets a pointer to private data on an object.
- [func JSObjectSetProperty(JSContextRef!, JSObjectRef!, JSStringRef!, JSValueRef!, JSPropertyAttributes, UnsafeMutablePointer<JSValueRef?>!)](jsobjectsetproperty(_:_:_:_:_:_:).md)
  Sets a property on an object.
- [func JSObjectSetPropertyAtIndex(JSContextRef!, JSObjectRef!, UInt32, JSValueRef!, UnsafeMutablePointer<JSValueRef?>!)](jsobjectsetpropertyatindex(_:_:_:_:_:).md)
  Sets a property on an object by numeric index.
- [func JSObjectGetPropertyForKey(JSContextRef!, JSObjectRef!, JSValueRef!, UnsafeMutablePointer<JSValueRef?>!) -> JSValueRef!](jsobjectgetpropertyforkey(_:_:_:_:).md)
  Gets a property from an object using a JavaScript value as the property key.
- [func JSObjectSetPrototype(JSContextRef!, JSObjectRef!, JSValueRef!)](jsobjectsetprototype(_:_:_:).md)
  Sets an object’s prototype.
- [func JSObjectDeletePropertyForKey(JSContextRef!, JSObjectRef!, JSValueRef!, UnsafeMutablePointer<JSValueRef?>!) -> Bool](jsobjectdeletepropertyforkey(_:_:_:_:).md)
  Deletes a property from an object using a JavaScript value as the property key.
- [func JSObjectHasPropertyForKey(JSContextRef!, JSObjectRef!, JSValueRef!, UnsafeMutablePointer<JSValueRef?>!) -> Bool](jsobjecthaspropertyforkey(_:_:_:_:).md)
  Tests whether an object has the specified property using a JavaScript value as the property key.
- [func JSObjectSetPropertyForKey(JSContextRef!, JSObjectRef!, JSValueRef!, JSValueRef!, JSPropertyAttributes, UnsafeMutablePointer<JSValueRef?>!)](jsobjectsetpropertyforkey(_:_:_:_:_:_:).md)
  Sets a property on an object using a JavaScript value as the property key.
- [func JSObjectMakeDeferredPromise(JSContextRef!, UnsafeMutablePointer<JSObjectRef?>!, UnsafeMutablePointer<JSObjectRef?>!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](jsobjectmakedeferredpromise(_:_:_:_:).md)
  Creates a JavaScript promise object by invoking the provided executor.
### Working with Classes
- [func JSClassCreate(UnsafePointer<JSClassDefinition>!) -> JSClassRef!](jsclasscreate(_:).md)
  Creates a JavaScript class.
- [func JSClassRelease(JSClassRef!)](jsclassrelease(_:).md)
  Releases a JavaScript class.
- [func JSClassRetain(JSClassRef!) -> JSClassRef!](jsclassretain(_:).md)
  Retains a JavaScript class.
- [let kJSClassDefinitionEmpty: JSClassDefinition](kjsclassdefinitionempty.md)
  A class definition structure of the current version that contains null pointers and has no attributes.
- [struct JSClassDefinition](jsclassdefinition.md)
  A structure that contains properties and callbacks that define a type of object.
- [JSClassAttribute](jsclassattribute.md)
  A JavaScript class attribute.
### Working with Properties
- [func JSPropertyNameAccumulatorAddName(JSPropertyNameAccumulatorRef!, JSStringRef!)](jspropertynameaccumulatoraddname(_:_:).md)
  Adds a property name to a JavaScript property name accumulator.
- [func JSPropertyNameArrayGetCount(JSPropertyNameArrayRef!) -> Int](jspropertynamearraygetcount(_:).md)
  Gets a count of the number of items in a JavaScript property name array.
- [func JSPropertyNameArrayGetNameAtIndex(JSPropertyNameArrayRef!, Int) -> JSStringRef!](jspropertynamearraygetnameatindex(_:_:).md)
  Gets a property name at a specified index in a JavaScript property name array.
- [func JSPropertyNameArrayRelease(JSPropertyNameArrayRef!)](jspropertynamearrayrelease(_:).md)
  Releases a JavaScript property name array.
- [func JSPropertyNameArrayRetain(JSPropertyNameArrayRef!) -> JSPropertyNameArrayRef!](jspropertynamearrayretain(_:).md)
  Retains a JavaScript property name array.
- [typealias JSPropertyAttributes](jspropertyattributes.md)
  A set of JavaScript property attributes.
- [JSPropertyAttribute](jspropertyattribute.md)
  A JavaScript property attribute.
- [typealias JSPropertyNameArrayRef](jspropertynamearrayref.md)
  An array of JavaScript property names.
- [typealias JSPropertyNameAccumulatorRef](jspropertynameaccumulatorref.md)
  An ordered set of the names of a JavaScript object’s properties.
### Creating a Typed Array
- [func JSObjectMakeTypedArray(JSContextRef!, JSTypedArrayType, Int, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](jsobjectmaketypedarray(_:_:_:_:).md)
  Creates a JavaScript typed array object with the specified number of elements.
- [func JSObjectMakeTypedArrayWithBytesNoCopy(JSContextRef!, JSTypedArrayType, UnsafeMutableRawPointer!, Int, JSTypedArrayBytesDeallocator!, UnsafeMutableRawPointer!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](jsobjectmaketypedarraywithbytesnocopy(_:_:_:_:_:_:_:).md)
  Creates a JavaScript typed array object from an existing pointer.
- [func JSObjectMakeTypedArrayWithArrayBuffer(JSContextRef!, JSTypedArrayType, JSObjectRef!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](jsobjectmaketypedarraywitharraybuffer(_:_:_:_:).md)
  Creates a JavaScript typed array object from an existing JavaScript array buffer object.
- [func JSObjectMakeTypedArrayWithArrayBufferAndOffset(JSContextRef!, JSTypedArrayType, JSObjectRef!, Int, Int, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](jsobjectmaketypedarraywitharraybufferandoffset(_:_:_:_:_:_:).md)
  Creates a JavaScript typed array object from an existing JavaScript array buffer object with the specified offset and length.
- [struct JSTypedArrayType](jstypedarraytype.md)
  The type of a JavaScript typed array object.
- [typealias JSTypedArrayBytesDeallocator](jstypedarraybytesdeallocator.md)
  A function that deallocates bytes that pass to a typed array constructor.
### Accessing Typed Array Information
- [func JSObjectGetTypedArrayBytesPtr(JSContextRef!, JSObjectRef!, UnsafeMutablePointer<JSValueRef?>!) -> UnsafeMutableRawPointer!](jsobjectgettypedarraybytesptr(_:_:_:).md)
  Returns a temporary pointer to the backing store of a JavaScript typed array object.
- [func JSObjectGetTypedArrayLength(JSContextRef!, JSObjectRef!, UnsafeMutablePointer<JSValueRef?>!) -> Int](jsobjectgettypedarraylength(_:_:_:).md)
  Returns the length of a JavaScript typed array object.
- [func JSObjectGetTypedArrayByteLength(JSContextRef!, JSObjectRef!, UnsafeMutablePointer<JSValueRef?>!) -> Int](jsobjectgettypedarraybytelength(_:_:_:).md)
  Returns the byte length of a JavaScript typed array object.
- [func JSObjectGetTypedArrayByteOffset(JSContextRef!, JSObjectRef!, UnsafeMutablePointer<JSValueRef?>!) -> Int](jsobjectgettypedarraybyteoffset(_:_:_:).md)
  Returns the byte offset of a JavaScript typed array object.
- [func JSObjectGetTypedArrayBuffer(JSContextRef!, JSObjectRef!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](jsobjectgettypedarraybuffer(_:_:_:).md)
  Returns the JavaScript array buffer object to use as the backing of a JavaScript typed array object.
### Working with Array Buffers
- [func JSObjectMakeArrayBufferWithBytesNoCopy(JSContextRef!, UnsafeMutableRawPointer!, Int, JSTypedArrayBytesDeallocator!, UnsafeMutableRawPointer!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](jsobjectmakearraybufferwithbytesnocopy(_:_:_:_:_:_:).md)
  Creates a JavaScript array buffer object from an existing pointer.
- [func JSObjectGetArrayBufferByteLength(JSContextRef!, JSObjectRef!, UnsafeMutablePointer<JSValueRef?>!) -> Int](jsobjectgetarraybufferbytelength(_:_:_:).md)
  Returns the number of bytes in a JavaScript data object.
- [func JSObjectGetArrayBufferBytesPtr(JSContextRef!, JSObjectRef!, UnsafeMutablePointer<JSValueRef?>!) -> UnsafeMutableRawPointer!](jsobjectgetarraybufferbytesptr(_:_:_:).md)
  Returns a pointer to the data buffer that serves as the backing store for a JavaScript typed array object.

## See Also

- [typealias JSValueRef](jsvalueref.md)
  A JavaScript value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsobjectref)*