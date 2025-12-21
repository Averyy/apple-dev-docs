# fileTransferWarningSize

**Framework**: TelephonyMessagingKit  
**Kind**: property

The size for issuing a warning about file transfers and Rich Card media objects.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
let fileTransferWarningSize: Measurement<UnitInformationStorage>?
```

#### Discussion

This value is equivalent to `FT WARN SIZE` in the RCS specification. Consult the specification for handling pre-recorded video that uses a resolution greater than 480p encoded at 1200 kbps. The specification’s guidance differs based on whether the file size is less than or greater than the warning size value. Your app may need to warn the person sending the video or force recompression to reduce its size.

This value is represented as a Foundation [`Measurement`](https://developer.apple.com/documentation/Foundation/Measurement) that uses the [`UnitInformationStorage`](https://developer.apple.com/documentation/Foundation/UnitInformationStorage) unit type. If the warning size isn’t applicable, the value is `nil`.

## See Also

- [var maximumFileTransferSize: Measurement<UnitInformationStorage>?](rcsservice/configuration/maximumfiletransfersize.md)
  The maximum size of a file that the RCS file transfer service can send.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/configuration/filetransferwarningsize)*