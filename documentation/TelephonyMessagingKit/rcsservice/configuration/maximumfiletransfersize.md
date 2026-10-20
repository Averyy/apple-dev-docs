# maximumFileTransferSize

**Framework**: TelephonyMessagingKit  
**Kind**: property  
**Role**: Instance Property

The maximum size of a file that the RCS file transfer service can send.

**Availability**:
- iOS 26.0+

## Declaration

```swift
var maximumFileTransferSize: Measurement<UnitInformationStorage>? { get }
```

#### Discussion

This value is represented as a Foundation [`Measurement`](../../../Foundation/measurement.md) that uses the [`UnitInformationStorage`](../../../Foundation/unitinformationstorage.md) unit type. If the messaging service doesn’t limit the file size, the value is `nil`.

## See Also

### Inspecting file transfer configuration
- [let fileTransferWarningSize: Measurement<UnitInformationStorage>?](./filetransferwarningsize.md)
  The size for issuing a warning about file transfers and Rich Card media objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/configuration/maximumfiletransfersize)*