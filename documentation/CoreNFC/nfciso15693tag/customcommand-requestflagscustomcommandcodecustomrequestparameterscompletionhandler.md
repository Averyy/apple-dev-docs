# customCommand(requestFlags:customCommandCode:customRequestParameters:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Required**: Yes

Sends a custom command (0xA0 to 0xDF command code), as defined in the ISO 15693-3 specification, to the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func customCommand(requestFlags flags: NFCISO15693RequestFlag, customCommandCode: Int, customRequestParameters: Data) async throws -> Data
```

#### Discussion

This method inserts the [`icManufacturerCode`](nfciso15693tag/icmanufacturercode.md) after the command byte before appending the `customRequestParameters` when constructing the data packet that the method sends to the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/customcommand(requestflags:customcommandcode:customrequestparameters:completionhandler:))*