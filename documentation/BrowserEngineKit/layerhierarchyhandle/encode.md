# encode(_:)

**Framework**: BrowserEngineKit  
**Kind**: method

Serializes the hierarchy handle into a Mach port reference and accompanying data.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
func encode(_ block: (mach_port_t, Data) -> Void)
```

#### Discussion

This method invokes the supplied closure with a `mach_port_t` and `Data` object that together represent the serialized layer hierarchy handle. The port serves as a reference to the layer hierarchy that you can share with another process. Use the port and data together to reconstruct the handle using [`init(port:data:)`](layerhierarchyhandle/init(port:data:).md).

```swift
handle.encode { port, data in
    guard port != MACH_PORT_NULL else {
        // The handle is already invalidated.
        return
    }
    
    // Send the port and data to the rendering process.
    sendToRenderingExtension(port: port, data: data)
    
    // Dispose of the port after sending.
    mach_port_deallocate(mach_task_self(), port)
}
```

> ❗ **Important**: Dispose of the Mach port in the supplied closure after sending it to the other process. The port is `MACH_PORT_NULL` if the handle has already been invalidated (see [`invalidate()`](layerhierarchy/invalidate().md)).

Each call to this method creates a new port reference and unique serialized data. Decode each port and data pair only once using [`init(port:data:)`](layerhierarchyhandle/init(port:data:).md).

## Parameters

- `block`: A closure that receives a Mach port and serialized data as arguments.

## See Also

- [init(port: mach_port_t, data: Data) throws](layerhierarchyhandle/init(port:data:).md)
  Creates a layer hierarchy handle using a Mach port reference and serialized data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchyhandle/encode(_:))*