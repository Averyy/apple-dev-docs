# device

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The digitizer that generates the touch. Useful to distinguish touches emanating from multiple-device scenarios.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var device: Any? { get }
```

```objc
@property (strong, readonly, nullable) id device;
```

## See Also

### Using Touch Device Properties
- [var deviceSize: NSSize](./devicesize.md)
  The range of the touch device in points, such as 72 ppi.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouch/device)*