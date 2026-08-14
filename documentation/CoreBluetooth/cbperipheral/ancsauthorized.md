# ancsAuthorized

**Framework**: Core Bluetooth  
**Kind**: property

A Boolean value that indicates if the remote device has authorization to receive data over ANCS protocol.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var ancsAuthorized: Bool { get }
```

#### Discussion

If this value is [`false`](https://developer.apple.com/documentation/swift/false), a user authorization sets this value to [`true`](https://developer.apple.com/documentation/swift/true), which results in a call to the delegate’s [`centralManager(_:didUpdateANCSAuthorizationFor:)`](cbcentralmanagerdelegate/centralmanager(_:didupdateancsauthorizationfor:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheral/ancsauthorized)*