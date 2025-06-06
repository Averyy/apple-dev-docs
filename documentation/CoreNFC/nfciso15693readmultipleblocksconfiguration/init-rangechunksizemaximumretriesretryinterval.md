# init(range:chunkSize:maximumRetries:retryInterval:)

**Framework**: Core NFC  
**Kind**: init

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(range: NSRange, chunkSize: Int, maximumRetries: Int, retryInterval: TimeInterval)
```

## Parameters

- `range`: Read range specify by the starting block index and the total number of blocks.
- `chunkSize`: Specify number of blocks parameter for the Read multiple blocks command.
- `maximumRetries`: Maximum number of retry attempt when tag response is not received.
- `retryInterval`: Time interval wait between each retry attempt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693readmultipleblocksconfiguration/init(range:chunksize:maximumretries:retryinterval:))*