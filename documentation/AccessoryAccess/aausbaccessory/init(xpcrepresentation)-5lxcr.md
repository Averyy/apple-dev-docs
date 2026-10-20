# init(XPCRepresentation:)

**Framework**: Accessory Access  
**Kind**: init  
**Role**: Initializer

Creates a USB accessory from an XPC representation.

**Availability**:
- macOS 27.0+

## Declaration

```swift
init?(XPCRepresentation xpcRepresentation: xpc_object_t)
```

#### Return Value

An `AAUSBAccessory` object if the framework decoded the provided `xpc_object_t`, or `nil` if it’s invalid.

## Parameters

- `xpcRepresentation`: The XPC representation of an `AAUSBAccessory` object received from the XPC.

## See Also

### Creating USB accessories
- [init?(xpcRepresentation: xpc_object_t)](./init%28xpcrepresentation%29-6dmbu.md)
  Creates a USB accessory from an XPC representation.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a new USB accessory with the provided coder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessory/init(xpcrepresentation:)-5lxcr)*