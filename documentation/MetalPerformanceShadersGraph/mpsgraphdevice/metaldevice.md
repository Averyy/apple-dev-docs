# metalDevice

**Framework**: Metal Performance Shaders Graph  
**Kind**: property  
**Role**: Instance Property

If device type is Metal then returns the corresponding MTLDevice else nil.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var metalDevice: (any MTLDevice)? { get }
```

```objc
@property (nonatomic, readonly, nullable) id<MTLDevice> metalDevice;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphdevice/metaldevice)*