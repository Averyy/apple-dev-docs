# JSObjectMakeTypedArrayWithArrayBufferAndOffset(_:_:_:_:_:_:)

**Framework**: JavaScriptCore  
**Kind**: func

Creates a JavaScript typed array object from an existing JavaScript array buffer object with the specified offset and length.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSObjectMakeTypedArrayWithArrayBufferAndOffset(_ ctx: JSContextRef!, _ arrayType: JSTypedArrayType, _ buffer: JSObjectRef!, _ byteOffset: Int, _ length: Int, _ exception: UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!
```

#### Return Value

A [`JSObjectRef`](jsobjectref.md) that is a typed array, or `NULL` if there is an error. The backing store of the typed array is `buffer`.

## Parameters

- `ctx`: The execution context to use.
- `arrayType`: A value that identifies the type of array to create. If   is   or  , this function returns  .
- `buffer`: An array buffer object to use as the backing store for the created JavaScript typed array object.
- `byteOffset`: The byte offset for the created typed array. Align   with the element size of  .
- `length`: The number of elements to include in the typed array.
- `exception`: A pointer to a   to store an exception in, if any. Pass   if you don’t want to store an exception.

## See Also

- [func JSObjectMakeTypedArray(JSContextRef!, JSTypedArrayType, Int, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](jsobjectmaketypedarray(_:_:_:_:).md)
  Creates a JavaScript typed array object with the specified number of elements.
- [func JSObjectMakeTypedArrayWithBytesNoCopy(JSContextRef!, JSTypedArrayType, UnsafeMutableRawPointer!, Int, JSTypedArrayBytesDeallocator!, UnsafeMutableRawPointer!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](jsobjectmaketypedarraywithbytesnocopy(_:_:_:_:_:_:_:).md)
  Creates a JavaScript typed array object from an existing pointer.
- [func JSObjectMakeTypedArrayWithArrayBuffer(JSContextRef!, JSTypedArrayType, JSObjectRef!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](jsobjectmaketypedarraywitharraybuffer(_:_:_:_:).md)
  Creates a JavaScript typed array object from an existing JavaScript array buffer object.
- [struct JSTypedArrayType](jstypedarraytype.md)
  The type of a JavaScript typed array object.
- [typealias JSTypedArrayBytesDeallocator](jstypedarraybytesdeallocator.md)
  A function that deallocates bytes that pass to a typed array constructor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsobjectmaketypedarraywitharraybufferandoffset(_:_:_:_:_:_:))*