# JSObjectGetTypedArrayByteLength(_:_:_:)

**Framework**: JavaScriptCore  
**Kind**: func

Returns the byte length of a JavaScript typed array object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSObjectGetTypedArrayByteLength(_ ctx: JSContextRef!, _ object: JSObjectRef!, _ exception: UnsafeMutablePointer<JSValueRef?>!) -> Int
```

#### Return Value

The byte length of the typed array object, or `0` if the object isn’t a typed array object.

## Parameters

- `ctx`: The execution context to use.
- `object`: The   with the typed array type data pointer to obtain.
- `exception`: A pointer to a   to store an exception in, if any. Pass   to discard any exception.

## See Also

- [func JSObjectGetTypedArrayBytesPtr(JSContextRef!, JSObjectRef!, UnsafeMutablePointer<JSValueRef?>!) -> UnsafeMutableRawPointer!](jsobjectgettypedarraybytesptr(_:_:_:).md)
  Returns a temporary pointer to the backing store of a JavaScript typed array object.
- [func JSObjectGetTypedArrayLength(JSContextRef!, JSObjectRef!, UnsafeMutablePointer<JSValueRef?>!) -> Int](jsobjectgettypedarraylength(_:_:_:).md)
  Returns the length of a JavaScript typed array object.
- [func JSObjectGetTypedArrayByteOffset(JSContextRef!, JSObjectRef!, UnsafeMutablePointer<JSValueRef?>!) -> Int](jsobjectgettypedarraybyteoffset(_:_:_:).md)
  Returns the byte offset of a JavaScript typed array object.
- [func JSObjectGetTypedArrayBuffer(JSContextRef!, JSObjectRef!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](jsobjectgettypedarraybuffer(_:_:_:).md)
  Returns the JavaScript array buffer object to use as the backing of a JavaScript typed array object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsobjectgettypedarraybytelength(_:_:_:))*