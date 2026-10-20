# device

**Framework**: Paravirtualized Graphics  
**Kind**: property  
**Role**: Instance Property

The Metal device object to use to back the virtual graphics device.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
var device: (any MTLDevice)? { get set }
```

```objc
@property (nonatomic, retain, readwrite, nullable) id<MTLDevice> device;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdevicedescriptor/device)*