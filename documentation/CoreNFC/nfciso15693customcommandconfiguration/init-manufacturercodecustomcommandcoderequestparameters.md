# init(manufacturerCode:customCommandCode:requestParameters:)

**Framework**: Core NFC  
**Kind**: init

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(manufacturerCode: Int, customCommandCode: Int, requestParameters: Data?)
```

#### Discussion

Initialize with default zero maximum retry and zero retry interval.

## Parameters

- `manufacturerCode`: 8 bits manufacturer code.
- `customCommandCode`: 8 bits custom command code.  Valid range is 0xA0 to 0xDF.
- `requestParameters`: Optional custom request parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693customcommandconfiguration/init(manufacturercode:customcommandcode:requestparameters:))*