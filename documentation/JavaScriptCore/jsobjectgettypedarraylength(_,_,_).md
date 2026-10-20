# JSObjectGetTypedArrayLength(_:_:_:)

**Framework**: JavaScriptCore  
**Kind**: func  
**Role**: Function

Returns the length of a JavaScript typed array object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSObjectGetTypedArrayLength(_ ctx: JSContextRef!, _ object: JSObjectRef!, _ exception: UnsafeMutablePointer<JSValueRef?>!) -> Int
```

```c
size_t JSObjectGetTypedArrayLength(JSContextRef ctx, JSObjectRef object, JSValueRef*exception);
```

#### Return Value

The length of the typed array object, or `0` if the object isn’t a typed array object.

## Parameters

- `ctx`: The execution context to use.
- `object`: The [`JSObjectRef`](./jsobjectref.md) with the typed array type data pointer to obtain.
- `exception`: A pointer to a [`JSValueRef`](./jsvalueref.md) to store an exception in, if any. Pass `NULL` to discard any exception.

## See Also

### Accessing Typed Array Information
- [func JSObjectGetTypedArrayBytesPtr(JSContextRef!, JSObjectRef!, UnsafeMutablePointer<JSValueRef?>!) -> UnsafeMutableRawPointer!](./jsobjectgettypedarraybytesptr%28_,_,_%29.md)
  Returns a temporary pointer to the backing store of a JavaScript typed array object.
- [func JSObjectGetTypedArrayByteLength(JSContextRef!, JSObjectRef!, UnsafeMutablePointer<JSValueRef?>!) -> Int](./jsobjectgettypedarraybytelength%28_,_,_%29.md)
  Returns the byte length of a JavaScript typed array object.
- [func JSObjectGetTypedArrayByteOffset(JSContextRef!, JSObjectRef!, UnsafeMutablePointer<JSValueRef?>!) -> Int](./jsobjectgettypedarraybyteoffset%28_,_,_%29.md)
  Returns the byte offset of a JavaScript typed array object.
- [func JSObjectGetTypedArrayBuffer(JSContextRef!, JSObjectRef!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](./jsobjectgettypedarraybuffer%28_,_,_%29.md)
  Returns the JavaScript array buffer object to use as the backing of a JavaScript typed array object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsobjectgettypedarraylength(_:_:_:))*