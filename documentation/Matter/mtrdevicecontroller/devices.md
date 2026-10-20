# devices

**Framework**: Matter  
**Kind**: property  
**Role**: Instance Property

Returns the list of MTRDevice instances that this controller has loaded into memory. Returns an empty array if no devices are in memory.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
var devices: [MTRDevice] { get }
```

```objc
@property (nonatomic, readonly) NSArray<MTRDevice *> * devices;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontroller/devices)*