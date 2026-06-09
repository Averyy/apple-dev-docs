# createXPCRepresentation()

**Framework**: Accessory Access  
**Kind**: method

Creates an encoded representation of the USB accessory.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func createXPCRepresentation() -> xpc_object_t
```

#### Discussion

A USB accessory can be encoded to [`xpc_object_t`](https://developer.apple.com/documentation/XPC/xpc_object_t), and passed to an XPC service over an XPC connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessory/createxpcrepresentation())*