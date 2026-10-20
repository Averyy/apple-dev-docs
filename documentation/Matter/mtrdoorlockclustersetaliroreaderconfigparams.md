# MTRDoorLockClusterSetAliroReaderConfigParams

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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
class MTRDoorLockClusterSetAliroReaderConfigParams
```

```objc
@interface MTRDoorLockClusterSetAliroReaderConfigParams : NSObject
```

## Topics

### Instance Properties
- [var groupIdentifier: Data](./mtrdoorlockclustersetaliroreaderconfigparams/groupidentifier.md)
- [var groupResolvingKey: Data?](./mtrdoorlockclustersetaliroreaderconfigparams/groupresolvingkey.md)
- [var serverSideProcessingTimeout: NSNumber?](./mtrdoorlockclustersetaliroreaderconfigparams/serversideprocessingtimeout.md)
  Controls how much time, in seconds, we will allow for the server to process the command.
- [var signingKey: Data](./mtrdoorlockclustersetaliroreaderconfigparams/signingkey.md)
- [var timedInvokeTimeoutMs: NSNumber?](./mtrdoorlockclustersetaliroreaderconfigparams/timedinvoketimeoutms.md)
  Controls whether the command is a timed command (using Timed Invoke).
- [var verificationKey: Data](./mtrdoorlockclustersetaliroreaderconfigparams/verificationkey.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdoorlockclustersetaliroreaderconfigparams)*