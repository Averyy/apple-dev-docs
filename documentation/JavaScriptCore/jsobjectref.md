# JSObjectRef

**Framework**: JavaScriptCore  
**Kind**: typealias  
**Role**: Type Alias

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

```c
typedef struct OpaqueJSValue * JSObjectRef;
```

#### Discussion

A [`JSObjectRef`](./jsobjectref.md) is a [`JSValueRef`](./jsvalueref.md).

## Topics

### Accessing the Global Object
- [func JSContextGetGlobalObject(JSContextRef!) -> JSObjectRef!](./jscontextgetglobalobject%28_%29.md)
  Gets the global object of a JavaScript execution context.
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
- [func JSObjectMakeError(JSContextRef!, Int, UnsafePointer<JSValueRef?>!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](./jsobjectmakeerror%28_,_,_,_%29.md)
  Creates a JavaScript error object as though invoking the built-in error constructor.
- [func JSObjectMakeFunction(JSContextRef!, JSStringRef!, UInt32, UnsafePointer<JSStringRef?>!, JSStringRef!, JSStringRef!, Int32, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](./jsobjectmakefunction%28_,_,_,_,_,_,_,_%29.md)
  Creates a function with a specified script as its body.
- [func JSObjectMakeFunctionWithCallback(JSContextRef!, JSStringRef!, JSObjectCallAsFunctionCallback!) -> JSObjectRef!](./jsobjectmakefunctionwithcallback%28_,_,_%29.md)
  Creates a JavaScript function with a specified callback as its implementation.
- [func JSObjectMakeRegExp(JSContextRef!, Int, UnsafePointer<JSValueRef?>!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](./jsobjectmakeregexp%28_,_,_,_%29.md)
  Creates a JavaScript regular expression object as though invoking the built-in regular expression constructor.
- [func JSObjectSetPrivate(JSObjectRef!, UnsafeMutableRawPointer!) -> Bool](./jsobjectsetprivate%28_,_%29.md)
  Sets a pointer to private data on an object.
- [func JSObjectSetProperty(JSContextRef!, JSObjectRef!, JSStringRef!, JSValueRef!, JSPropertyAttributes, UnsafeMutablePointer<JSValueRef?>!)](./jsobjectsetproperty%28_,_,_,_,_,_%29.md)
  Sets a property on an object.
- [func JSObjectSetPropertyAtIndex(JSContextRef!, JSObjectRef!, UInt32, JSValueRef!, UnsafeMutablePointer<JSValueRef?>!)](./jsobjectsetpropertyatindex%28_,_,_,_,_%29.md)
  Sets a property on an object by numeric index.
- [func JSObjectGetPropertyForKey(JSContextRef!, JSObjectRef!, JSValueRef!, UnsafeMutablePointer<JSValueRef?>!) -> JSValueRef!](./jsobjectgetpropertyforkey%28_,_,_,_%29.md)
  Gets a property from an object using a JavaScript value as the property key.
- [func JSObjectSetPrototype(JSContextRef!, JSObjectRef!, JSValueRef!)](./jsobjectsetprototype%28_,_,_%29.md)
  Sets an object’s prototype.
- [func JSObjectDeletePropertyForKey(JSContextRef!, JSObjectRef!, JSValueRef!, UnsafeMutablePointer<JSValueRef?>!) -> Bool](./jsobjectdeletepropertyforkey%28_,_,_,_%29.md)
  Deletes a property from an object using a JavaScript value as the property key.
- [func JSObjectHasPropertyForKey(JSContextRef!, JSObjectRef!, JSValueRef!, UnsafeMutablePointer<JSValueRef?>!) -> Bool](./jsobjecthaspropertyforkey%28_,_,_,_%29.md)
  Tests whether an object has the specified property using a JavaScript value as the property key.
- [func JSObjectSetPropertyForKey(JSContextRef!, JSObjectRef!, JSValueRef!, JSValueRef!, JSPropertyAttributes, UnsafeMutablePointer<JSValueRef?>!)](./jsobjectsetpropertyforkey%28_,_,_,_,_,_%29.md)
  Sets a property on an object using a JavaScript value as the property key.
- [func JSObjectMakeDeferredPromise(JSContextRef!, UnsafeMutablePointer<JSObjectRef?>!, UnsafeMutablePointer<JSObjectRef?>!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](./jsobjectmakedeferredpromise%28_,_,_,_%29.md)
  Creates a JavaScript promise object by invoking the provided executor.
### Working with Classes
- [func JSClassCreate(UnsafePointer<JSClassDefinition>!) -> JSClassRef!](./jsclasscreate%28_%29.md)
  Creates a JavaScript class.
- [func JSClassRelease(JSClassRef!)](./jsclassrelease%28_%29.md)
  Releases a JavaScript class.
- [func JSClassRetain(JSClassRef!) -> JSClassRef!](./jsclassretain%28_%29.md)
  Retains a JavaScript class.
- [let kJSClassDefinitionEmpty: JSClassDefinition](./kjsclassdefinitionempty.md)
  A class definition structure of the current version that contains null pointers and has no attributes.
- [struct JSClassDefinition](./jsclassdefinition.md)
  A structure that contains properties and callbacks that define a type of object.
- [JSClassAttribute](./jsclassattribute.md)
  A JavaScript class attribute.
### Working with Properties
- [func JSPropertyNameAccumulatorAddName(JSPropertyNameAccumulatorRef!, JSStringRef!)](./jspropertynameaccumulatoraddname%28_,_%29.md)
  Adds a property name to a JavaScript property name accumulator.
- [func JSPropertyNameArrayGetCount(JSPropertyNameArrayRef!) -> Int](./jspropertynamearraygetcount%28_%29.md)
  Gets a count of the number of items in a JavaScript property name array.
- [func JSPropertyNameArrayGetNameAtIndex(JSPropertyNameArrayRef!, Int) -> JSStringRef!](./jspropertynamearraygetnameatindex%28_,_%29.md)
  Gets a property name at a specified index in a JavaScript property name array.
- [func JSPropertyNameArrayRelease(JSPropertyNameArrayRef!)](./jspropertynamearrayrelease%28_%29.md)
  Releases a JavaScript property name array.
- [func JSPropertyNameArrayRetain(JSPropertyNameArrayRef!) -> JSPropertyNameArrayRef!](./jspropertynamearrayretain%28_%29.md)
  Retains a JavaScript property name array.
- [typealias JSPropertyAttributes](./jspropertyattributes.md)
  A set of JavaScript property attributes.
- [JSPropertyAttribute](./jspropertyattribute.md)
  A JavaScript property attribute.
- [typealias JSPropertyNameArrayRef](./jspropertynamearrayref.md)
  An array of JavaScript property names.
- [typealias JSPropertyNameAccumulatorRef](./jspropertynameaccumulatorref.md)
  An ordered set of the names of a JavaScript object’s properties.
### Creating a Typed Array
- [func JSObjectMakeTypedArray(JSContextRef!, JSTypedArrayType, Int, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](./jsobjectmaketypedarray%28_,_,_,_%29.md)
  Creates a JavaScript typed array object with the specified number of elements.
- [func JSObjectMakeTypedArrayWithBytesNoCopy(JSContextRef!, JSTypedArrayType, UnsafeMutableRawPointer!, Int, JSTypedArrayBytesDeallocator!, UnsafeMutableRawPointer!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](./jsobjectmaketypedarraywithbytesnocopy%28_,_,_,_,_,_,_%29.md)
  Creates a JavaScript typed array object from an existing pointer.
- [func JSObjectMakeTypedArrayWithArrayBuffer(JSContextRef!, JSTypedArrayType, JSObjectRef!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](./jsobjectmaketypedarraywitharraybuffer%28_,_,_,_%29.md)
  Creates a JavaScript typed array object from an existing JavaScript array buffer object.
- [func JSObjectMakeTypedArrayWithArrayBufferAndOffset(JSContextRef!, JSTypedArrayType, JSObjectRef!, Int, Int, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](./jsobjectmaketypedarraywitharraybufferandoffset%28_,_,_,_,_,_%29.md)
  Creates a JavaScript typed array object from an existing JavaScript array buffer object with the specified offset and length.
- [struct JSTypedArrayType](./jstypedarraytype.md)
  The type of a JavaScript typed array object.
- [typealias JSTypedArrayBytesDeallocator](./jstypedarraybytesdeallocator.md)
  A function that deallocates bytes that pass to a typed array constructor.
### Accessing Typed Array Information
- [func JSObjectGetTypedArrayBytesPtr(JSContextRef!, JSObjectRef!, UnsafeMutablePointer<JSValueRef?>!) -> UnsafeMutableRawPointer!](./jsobjectgettypedarraybytesptr%28_,_,_%29.md)
  Returns a temporary pointer to the backing store of a JavaScript typed array object.
- [func JSObjectGetTypedArrayLength(JSContextRef!, JSObjectRef!, UnsafeMutablePointer<JSValueRef?>!) -> Int](./jsobjectgettypedarraylength%28_,_,_%29.md)
  Returns the length of a JavaScript typed array object.
- [func JSObjectGetTypedArrayByteLength(JSContextRef!, JSObjectRef!, UnsafeMutablePointer<JSValueRef?>!) -> Int](./jsobjectgettypedarraybytelength%28_,_,_%29.md)
  Returns the byte length of a JavaScript typed array object.
- [func JSObjectGetTypedArrayByteOffset(JSContextRef!, JSObjectRef!, UnsafeMutablePointer<JSValueRef?>!) -> Int](./jsobjectgettypedarraybyteoffset%28_,_,_%29.md)
  Returns the byte offset of a JavaScript typed array object.
- [func JSObjectGetTypedArrayBuffer(JSContextRef!, JSObjectRef!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](./jsobjectgettypedarraybuffer%28_,_,_%29.md)
  Returns the JavaScript array buffer object to use as the backing of a JavaScript typed array object.
### Working with Array Buffers
- [func JSObjectMakeArrayBufferWithBytesNoCopy(JSContextRef!, UnsafeMutableRawPointer!, Int, JSTypedArrayBytesDeallocator!, UnsafeMutableRawPointer!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](./jsobjectmakearraybufferwithbytesnocopy%28_,_,_,_,_,_%29.md)
  Creates a JavaScript array buffer object from an existing pointer.
- [func JSObjectGetArrayBufferByteLength(JSContextRef!, JSObjectRef!, UnsafeMutablePointer<JSValueRef?>!) -> Int](./jsobjectgetarraybufferbytelength%28_,_,_%29.md)
  Returns the number of bytes in a JavaScript data object.
- [func JSObjectGetArrayBufferBytesPtr(JSContextRef!, JSObjectRef!, UnsafeMutablePointer<JSValueRef?>!) -> UnsafeMutableRawPointer!](./jsobjectgetarraybufferbytesptr%28_,_,_%29.md)
  Returns a pointer to the data buffer that serves as the backing store for a JavaScript typed array object.

## See Also

### JavaScript Data Types
- [typealias JSValueRef](./jsvalueref.md)
  A JavaScript value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsobjectref)*