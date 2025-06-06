# setIdleTimeout(_:)

**Framework**: IOUSBHost  
**Kind**: method

Sets the desired idle suspend timeout for the interface.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func setIdleTimeout(_ idleTimeout: TimeInterval) throws
```

#### Discussion

After the interface idles, it defers electrical suspension of the device for the specified duration.

## Parameters

- `idleTimeout`: The amount of time after all pipes are idle to wait before suspending the device.

## See Also

- [var idleTimeout: TimeInterval](iousbhostinterface/idletimeout.md)
  The current idle suspend timeout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostinterface/setidletimeout(_:))*