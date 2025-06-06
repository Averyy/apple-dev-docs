# sendCustomCommand(commandConfiguration:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Required**: Yes

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func sendCustomCommand(commandConfiguration: NFCISO15693CustomCommandConfiguration, completionHandler: @escaping (Data, (any Error)?) -> Void)
```

#### Discussion

Send a manufacturer dependent custom command using command code range from 0xA0 to 0xDF.  Refer to ISO15693-3 specification for details.

## Parameters

- `commandConfiguration`: Configuration for the Manufacturer Custom Command.
- `completionHandler`: Completion handler called when the operation is completed.  error is nil if operation succeeds.   A @link NFCISO15693TagResponseErrorKey @link/ in NSError userInfo dictionary is returned when the tag   responded to the command with an error, and the error code value is defined in ISO15693-3 specification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/sendcustomcommand(commandconfiguration:completionhandler:))*