# SCDynamicStoreCreate(_:_:_:_:)

**Framework**: System Configuration  
**Kind**: func

Creates a new session used to interact with the dynamic store maintained by the System Configuration server.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCDynamicStoreCreate(_ allocator: CFAllocator?, _ name: CFString, _ callout: SCDynamicStoreCallBack?, _ context: UnsafeMutablePointer<SCDynamicStoreContext>?) -> SCDynamicStore?
```

#### Return Value

A reference to the new dynamic store session. You must release the returned value.

## Parameters

- `allocator`: The allocator that should be used to allocate memory for the local dynamic store object. This parameter may be   in which case the current default allocator is used. If this value is not a valid  , the behavior is undefined.
- `name`: The name of the calling process or plug-in of the caller.
- `callout`: The function to be called when a watched value in the dynamic store is changed. Pass   if no callouts are desired.
- `context`: The context associated with the callout. See   for more information about this value.

## See Also

- [func SCDynamicStoreCreateWithOptions(CFAllocator?, CFString, CFDictionary?, SCDynamicStoreCallBack?, UnsafeMutablePointer<SCDynamicStoreContext>?) -> SCDynamicStore?](scdynamicstorecreatewithoptions(_:_:_:_:_:).md)
  Creates a new session used to interact with the dynamic store maintained by the System Configuration server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecreate(_:_:_:_:))*