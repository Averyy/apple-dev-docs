# JSTypedArrayBytesDeallocator

**Framework**: JavaScriptCore  
**Kind**: typealias

A function that deallocates bytes that pass to a typed array constructor.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
typealias JSTypedArrayBytesDeallocator = (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Void
```

## Parameters

- `bytes`: A pointer to the bytes that originally pass to the typed array constructor.
- `deallocatorContext  `: A pointer to additional information to use when freeing the bytes.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jstypedarraybytesdeallocator)*