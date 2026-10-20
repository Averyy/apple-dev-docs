# NFCISO15693CustomCommandConfiguration

**Framework**: Core NFC  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class NFCISO15693CustomCommandConfiguration
```

```objc
@interface NFCISO15693CustomCommandConfiguration : NFCTagCommandConfiguration
```

#### Overview

Configuration options for the Manufacturer Custom command.

## Topics

### Initializers
- [init(manufacturerCode: Int, customCommandCode: Int, requestParameters: Data?)](./nfciso15693customcommandconfiguration/init%28manufacturercode,customcommandcode,requestparameters%29.md)
- [init(manufacturerCode: Int, customCommandCode: Int, requestParameters: Data?, maximumRetries: Int, retryInterval: TimeInterval)](./nfciso15693customcommandconfiguration/init%28manufacturercode,customcommandcode,requestparameters,maximumretries,retryinterval%29.md)
### Instance Properties
- [var customCommandCode: Int](./nfciso15693customcommandconfiguration/customcommandcode.md)
- [var manufacturerCode: Int](./nfciso15693customcommandconfiguration/manufacturercode.md)
- [var requestParameters: Data](./nfciso15693customcommandconfiguration/requestparameters.md)

## Relationships

### Inherits From
- [NFCTagCommandConfiguration](./nfctagcommandconfiguration.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693customcommandconfiguration)*