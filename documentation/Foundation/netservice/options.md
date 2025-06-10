# NetService.Options

**Framework**: Foundation  
**Kind**: struct

These constants specify options for a network service.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct Options
```

## Topics

### Constants
- [static var noAutoRename: NetService.Options](netservice/options/noautorename.md)
  Specifies that the network service should not rename itself in the event of a name collision.
- [static var listenForConnections: NetService.Options](netservice/options/listenforconnections.md)
- [static var noAutoRename: NetService.Options](netservice/options/noautorename.md)
  Specifies that the network service should not rename itself in the event of a name collision.
- [static var listenForConnections: NetService.Options](netservice/options/listenforconnections.md)
### Initializers
- [init(rawValue: UInt)](netservice/options/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [NSNetServices Errors](nsnetservices-errors.md)
  If an error occurs, the delegate error-handling methods return a dictionary with the following keys.
- [NetService.ErrorCode](netservice/errorcode-swift.enum.md)
  These constants identify errors that can occur when accessing net services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice/options)*