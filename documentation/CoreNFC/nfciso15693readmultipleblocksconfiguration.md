# NFCISO15693ReadMultipleBlocksConfiguration

**Framework**: Core NFC  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class NFCISO15693ReadMultipleBlocksConfiguration
```

```objc
@interface NFCISO15693ReadMultipleBlocksConfiguration : NFCTagCommandConfiguration
```

## Overview

Configuration options for the Read Multiple Blocks command.

## Topics

### Initializers
- [init(range: NSRange, chunkSize: Int)](./nfciso15693readmultipleblocksconfiguration/init%28range,chunksize%29.md)
- [init(range: NSRange, chunkSize: Int, maximumRetries: Int, retryInterval: TimeInterval)](./nfciso15693readmultipleblocksconfiguration/init%28range,chunksize,maximumretries,retryinterval%29.md)
### Instance Properties
- [var chunkSize: Int](./nfciso15693readmultipleblocksconfiguration/chunksize.md)
- [var range: NSRange](./nfciso15693readmultipleblocksconfiguration/range.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693readmultipleblocksconfiguration)*