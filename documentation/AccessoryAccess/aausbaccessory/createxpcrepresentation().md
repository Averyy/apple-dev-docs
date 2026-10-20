# createXPCRepresentation()

**Framework**: Accessory Access  
**Kind**: method  
**Role**: Instance Method

Creates an encoded representation of the USB accessory.

**Availability**:
- macOS 27.0+

## Declaration

```swift
func createXPCRepresentation() -> xpc_object_t
```

```objc
- (xpc_object_t) createXPCRepresentation;
```

#### Discussion

A USB accessory can be encoded to [`xpc_object_t`](../../XPC/xpc_object_t.md), and passed to an XPC service over an XPC connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessory/createxpcrepresentation())*