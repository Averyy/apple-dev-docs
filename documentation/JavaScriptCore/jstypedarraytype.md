# JSTypedArrayType

**Framework**: JavaScriptCore  
**Kind**: struct

The type of a JavaScript typed array object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct JSTypedArrayType
```

## Topics

### Constants
- [var kJSTypedArrayTypeNone: JSTypedArrayType](kjstypedarraytypenone.md)
  Not a typed array.
- [var kJSTypedArrayTypeArrayBuffer: JSTypedArrayType](kjstypedarraytypearraybuffer.md)
  An array buffer type.
- [var kJSTypedArrayTypeInt8Array: JSTypedArrayType](kjstypedarraytypeint8array.md)
  An 8-bit integer array type.
- [var kJSTypedArrayTypeInt16Array: JSTypedArrayType](kjstypedarraytypeint16array.md)
  A 16-bit integer array type.
- [var kJSTypedArrayTypeInt32Array: JSTypedArrayType](kjstypedarraytypeint32array.md)
  A 32-bit integer array type.
- [var kJSTypedArrayTypeBigInt64Array: JSTypedArrayType](kjstypedarraytypebigint64array.md)
- [var kJSTypedArrayTypeUint8Array: JSTypedArrayType](kjstypedarraytypeuint8array.md)
  An 8-bit unsigned integer array type.
- [var kJSTypedArrayTypeUint8ClampedArray: JSTypedArrayType](kjstypedarraytypeuint8clampedarray.md)
  An 8-bit unsigned integer clamped array type.
- [var kJSTypedArrayTypeUint16Array: JSTypedArrayType](kjstypedarraytypeuint16array.md)
  A 16-bit unsigned integer array type.
- [var kJSTypedArrayTypeUint32Array: JSTypedArrayType](kjstypedarraytypeuint32array.md)
  A 32-bit unsigned integer array type.
- [var kJSTypedArrayTypeBigUint64Array: JSTypedArrayType](kjstypedarraytypebiguint64array.md)
- [var kJSTypedArrayTypeFloat32Array: JSTypedArrayType](kjstypedarraytypefloat32array.md)
  A 32-bit floating point array type.
- [var kJSTypedArrayTypeFloat64Array: JSTypedArrayType](kjstypedarraytypefloat64array.md)
  A 64-bit floating point array type.
### Initializers
- [init(UInt32)](jstypedarraytype/init(_:).md)
  Creates a typed array.
- [init(rawValue: UInt32)](jstypedarraytype/init(rawvalue:).md)
  Creates a typed array with the specified raw value.
- [var rawValue: UInt32](jstypedarraytype/rawvalue.md)
  The raw value that represents the typed array’s type.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func JSObjectMakeTypedArray(JSContextRef!, JSTypedArrayType, Int, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](jsobjectmaketypedarray(_:_:_:_:).md)
  Creates a JavaScript typed array object with the specified number of elements.
- [func JSObjectMakeTypedArrayWithBytesNoCopy(JSContextRef!, JSTypedArrayType, UnsafeMutableRawPointer!, Int, JSTypedArrayBytesDeallocator!, UnsafeMutableRawPointer!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](jsobjectmaketypedarraywithbytesnocopy(_:_:_:_:_:_:_:).md)
  Creates a JavaScript typed array object from an existing pointer.
- [func JSObjectMakeTypedArrayWithArrayBuffer(JSContextRef!, JSTypedArrayType, JSObjectRef!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](jsobjectmaketypedarraywitharraybuffer(_:_:_:_:).md)
  Creates a JavaScript typed array object from an existing JavaScript array buffer object.
- [func JSObjectMakeTypedArrayWithArrayBufferAndOffset(JSContextRef!, JSTypedArrayType, JSObjectRef!, Int, Int, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](jsobjectmaketypedarraywitharraybufferandoffset(_:_:_:_:_:_:).md)
  Creates a JavaScript typed array object from an existing JavaScript array buffer object with the specified offset and length.
- [typealias JSTypedArrayBytesDeallocator](jstypedarraybytesdeallocator.md)
  A function that deallocates bytes that pass to a typed array constructor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jstypedarraytype)*