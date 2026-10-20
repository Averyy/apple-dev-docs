# pairDevice(_:address:port:setupPINCode:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.1+ - Deprecated in 16.4
- iPadOS 16.1+ - Deprecated in 16.4
- Mac Catalyst 16.1+ - Deprecated in 16.4
- macOS 13.0+ - Deprecated in 13.3
- tvOS 16.1+ - Deprecated in 16.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.1+ - Deprecated in 9.4

> **Deprecated**: Please use setupCommissioningSessionWithPayload:newNodeID:error:

## Declaration

```swift
func pairDevice(_ deviceID: UInt64, address: String, port: UInt16, setupPINCode: UInt32) throws
```

```objc
- (BOOL) pairDevice:(uint64_t) deviceID address:(NSString *) address port:(uint16_t) port setupPINCode:(uint32_t) setupPINCode error:(NSError **) error;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontroller/pairdevice(_:address:port:setuppincode:))*