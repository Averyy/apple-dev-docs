# customCommand(requestFlags:customCommandCode:customRequestParameters:resultHandler:)

**Framework**: Core NFC  
**Kind**: method

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+

## Declaration

```swift
func customCommand(requestFlags flags: NFCISO15693RequestFlag, customCommandCode: Int, customRequestParameters: Data, resultHandler: @escaping (Result<Data, any Error>) -> Void)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/customcommand(requestflags:customcommandcode:customrequestparameters:resulthandler:))*