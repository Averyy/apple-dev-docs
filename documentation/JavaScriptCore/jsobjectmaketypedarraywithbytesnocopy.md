# JSObjectMakeTypedArrayWithBytesNoCopy(_:_:_:_:_:_:_:)

**Framework**: JavaScriptCore  
**Kind**: func

Creates a JavaScript typed array object from an existing pointer.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSObjectMakeTypedArrayWithBytesNoCopy(_ ctx: JSContextRef!, _ arrayType: JSTypedArrayType, _ bytes: UnsafeMutableRawPointer!, _ byteLength: Int, _ bytesDeallocator: JSTypedArrayBytesDeallocator!, _ deallocatorContext: UnsafeMutableRawPointer!, _ exception: UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!
```

#### Return Value

A [`JSObjectRef`](jsobjectref.md) typed array with a backing store that is the same as the one that `bytes` points to, or `NULL` if there is an error.

#### Discussion

If the system throws an exception during this function, it always calls the `bytesDeallocator`.

## Parameters

- `ctx`: The execution context to use.
- `arrayType`: A value that identifies the type of array to create. If   is   or  , this function returns  .
- `bytes`: A pointer to the byte buffer to use as the backing store of the typed array object.
- `byteLength`: The number of bytes that   points to.
- `bytesDeallocator`: The allocator to use to deallocate the external buffer when deallocating the typed array object.
- `deallocatorContext`: A pointer to pass back to the deallocator.
- `exception`: A pointer to a   to store an exception in, if any. Pass   if you don’t want to store an exception.

## See Also

- [func JSObjectMakeTypedArray(JSContextRef!, JSTypedArrayType, Int, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](jsobjectmaketypedarray(_:_:_:_:).md)
  Creates a JavaScript typed array object with the specified number of elements.
- [func JSObjectMakeTypedArrayWithArrayBuffer(JSContextRef!, JSTypedArrayType, JSObjectRef!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](jsobjectmaketypedarraywitharraybuffer(_:_:_:_:).md)
  Creates a JavaScript typed array object from an existing JavaScript array buffer object.
- [func JSObjectMakeTypedArrayWithArrayBufferAndOffset(JSContextRef!, JSTypedArrayType, JSObjectRef!, Int, Int, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](jsobjectmaketypedarraywitharraybufferandoffset(_:_:_:_:_:_:).md)
  Creates a JavaScript typed array object from an existing JavaScript array buffer object with the specified offset and length.
- [struct JSTypedArrayType](jstypedarraytype.md)
  The type of a JavaScript typed array object.
- [typealias JSTypedArrayBytesDeallocator](jstypedarraybytesdeallocator.md)
  A function that deallocates bytes that pass to a typed array constructor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsobjectmaketypedarraywithbytesnocopy(_:_:_:_:_:_:_:))*