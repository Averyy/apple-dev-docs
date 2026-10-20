# dispatchType

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The strategy for dispatching any compute commands encoded in the compute pass.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var dispatchType: MTLDispatchType { get set }
```

```objc
@property (nonatomic) MTLDispatchType dispatchType;
```

#### Discussion

The default dispatch type is [`MTLDispatchType.serial`](../mtldispatchtype/serial.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepassdescriptor/dispatchtype)*