# maximumFileTransferSize

**Framework**: TelephonyMessagingKit  
**Kind**: property

The maximum size of a file that the RCS file transfer service can send.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
var maximumFileTransferSize: Measurement<UnitInformationStorage>? { get }
```

#### Discussion

This value is represented as a Foundation [`Measurement`](https://developer.apple.com/documentation/Foundation/Measurement) that uses the [`UnitInformationStorage`](https://developer.apple.com/documentation/Foundation/UnitInformationStorage) unit type. If the messaging service doesn’t limit the file size, the value is `nil`.

## See Also

- [let fileTransferWarningSize: Measurement<UnitInformationStorage>?](rcsservice/configuration/filetransferwarningsize.md)
  The size for issuing a warning about file transfers and Rich Card media objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/configuration/maximumfiletransfersize)*