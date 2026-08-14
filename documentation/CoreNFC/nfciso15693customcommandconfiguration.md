# NFCISO15693CustomCommandConfiguration

**Framework**: Core NFC  
**Kind**: class

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class NFCISO15693CustomCommandConfiguration
```

#### Overview

Configuration options for the Manufacturer Custom command.

## Topics

### Initializers
- [init(manufacturerCode: Int, customCommandCode: Int, requestParameters: Data?)](nfciso15693customcommandconfiguration/init(manufacturercode:customcommandcode:requestparameters:).md)
- [init(manufacturerCode: Int, customCommandCode: Int, requestParameters: Data?, maximumRetries: Int, retryInterval: TimeInterval)](nfciso15693customcommandconfiguration/init(manufacturercode:customcommandcode:requestparameters:maximumretries:retryinterval:).md)
### Instance Properties
- [var customCommandCode: Int](nfciso15693customcommandconfiguration/customcommandcode.md)
- [var manufacturerCode: Int](nfciso15693customcommandconfiguration/manufacturercode.md)
- [var requestParameters: Data](nfciso15693customcommandconfiguration/requestparameters.md)

## Relationships

### Inherits From
- [NFCTagCommandConfiguration](nfctagcommandconfiguration.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693customcommandconfiguration)*