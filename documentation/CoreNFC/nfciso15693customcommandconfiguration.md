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
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693customcommandconfiguration)*