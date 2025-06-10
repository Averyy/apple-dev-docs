# CBManagerAuthorization

**Framework**: Core Bluetooth  
**Kind**: enum

The current authorization state of a Core Bluetooth manager.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum CBManagerAuthorization
```

## Topics

### Authorization States
- [CBManagerAuthorization.allowedAlways](cbmanagerauthorization/allowedalways.md)
  A state that indicates the user has authorized Bluetooth at any time.
- [CBManagerAuthorization.denied](cbmanagerauthorization/denied.md)
  A state that indicates the user explicitly denied Bluetooth access for this app.
- [CBManagerAuthorization.notDetermined](cbmanagerauthorization/notdetermined.md)
  A state that indicates the user has yet to authorize Bluetooth for this app.
- [CBManagerAuthorization.restricted](cbmanagerauthorization/restricted.md)
  A state that indicates this app isn’t authorized to use Bluetooth.
### Initializers
- [init?(rawValue: Int)](cbmanagerauthorization/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class var authorization: CBManagerAuthorization](cbmanager/authorization-swift.type.property.md)
  The current authorization status for using Bluetooth.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbmanagerauthorization)*