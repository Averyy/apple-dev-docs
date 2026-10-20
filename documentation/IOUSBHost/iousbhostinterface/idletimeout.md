# idleTimeout

**Framework**: IOUSBHost  
**Kind**: property  
**Role**: Instance Property

The current idle suspend timeout.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
var idleTimeout: TimeInterval { get }
```

```objc
@property (readonly) NSTimeInterval idleTimeout;
```

#### Return Value

The amount of time after all pipes are idle to wait before suspending the device.

## See Also

### Enabling Power Savings
- [func setIdleTimeout(TimeInterval) throws](./setidletimeout%28_%29.md)
  Sets the desired idle suspend timeout for the interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostinterface/idletimeout)*