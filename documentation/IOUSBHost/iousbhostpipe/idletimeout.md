# idleTimeout

**Framework**: IOUSBHost  
**Kind**: property

A property that retrieves the current idle suspend timeout.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
var idleTimeout: TimeInterval { get }
```

#### Return Value

The amount of time after all pipes are idle to wait before suspending the device.

## See Also

- [func setIdleTimeout(TimeInterval) throws](iousbhostpipe/setidletimeout(_:).md)
  Sets the desired idle suspend timeout for the interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostpipe/idletimeout)*