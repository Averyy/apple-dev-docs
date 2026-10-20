# NetService.Options

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

```c
enum NSNetServiceOptions : NSUInteger;
```

## Topics

### Constants
- [static var noAutoRename: NetService.Options](./options/noautorename.md)
  Specifies that the network service should not rename itself in the event of a name collision.
- [static var listenForConnections: NetService.Options](./options/listenforconnections.md)
### Initializers
- [init(rawValue: UInt)](./options/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Constants
- [NSNetServices Errors](../nsnetservices-errors.md)
  If an error occurs, the delegate error-handling methods return a dictionary with the following keys.
- [NetService.ErrorCode](./errorcode-swift.enum.md)
  These constants identify errors that can occur when accessing net services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice/options)*