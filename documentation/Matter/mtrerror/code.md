# MTRError.Code

**Framework**: Matter  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+
- watchOS 9.1+

## Declaration

```swift
enum Code
```

```c
enum MTRErrorCode : NSInteger;
```

## Topics

### Enumeration Cases
- [MTRError.Code.bufferTooSmall](./code/buffertoosmall.md)
- [MTRError.Code.cancelled](./code/cancelled.md)
- [MTRError.Code.dnssdUnauthorized](./code/dnssdunauthorized.md)
- [MTRError.Code.fabricExists](./code/fabricexists.md)
- [MTRError.Code.generalError](./code/generalerror.md)
- [MTRError.Code.integrityCheckFailed](./code/integritycheckfailed.md)
- [MTRError.Code.invalidArgument](./code/invalidargument.md)
- [MTRError.Code.invalidIntegerValue](./code/invalidintegervalue.md)
- [MTRError.Code.invalidMessageLength](./code/invalidmessagelength.md)
- [MTRError.Code.invalidState](./code/invalidstate.md)
- [MTRError.Code.invalidStringLength](./code/invalidstringlength.md)
- [MTRError.Code.schemaMismatch](./code/schemamismatch.md)
- [MTRError.Code.timeout](./code/timeout.md)
- [MTRError.Code.tlvDecodeFailed](./code/tlvdecodefailed.md)
- [MTRError.Code.unknownSchema](./code/unknownschema.md)
- [MTRError.Code.wrongAddressType](./code/wrongaddresstype.md)
- [MTRError.Code.accessDenied](./code/accessdenied.md)
  Access to some resource was denied.
- [MTRError.Code.busy](./code/busy.md)
  A request was made to some entity, and that entity cannot handle the request right now, but might be able to at a different point in time.
- [MTRError.Code.notFound](./code/notfound.md)
  Something was requested that could not be located.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrerror/code)*