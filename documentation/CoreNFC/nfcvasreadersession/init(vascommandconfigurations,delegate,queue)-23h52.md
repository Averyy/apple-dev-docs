# init(vasCommandConfigurations:delegate:queue:)

**Framework**: Core NFC  
**Kind**: init  
**Role**: Initializer

Creates a VAS reader session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(vasCommandConfigurations commandConfigurations: [NFCVASCommandConfiguration], delegate: any NFCVASReaderSessionDelegate, queue: dispatch_queue_t?)
```

```objc
- (instancetype) initWithVASCommandConfigurations:(NSArray<NFCVASCommandConfiguration *> *) commandConfigurations delegate:(id<NFCVASReaderSessionDelegate>) delegate queue:(dispatch_queue_t) queue;
```

#### Return Value

A newly initialized VAS reader session object.

## See Also

### Creating a VAS Reader Session
- [class NFCVASCommandConfiguration](../nfcvascommandconfiguration.md)
  An object providing the configuration for a GET VAS DATA command.
- [protocol NFCVASReaderSessionDelegate](../nfcvasreadersessiondelegate.md)
  A protocol that an object implements to receive callbacks from a VAS reader session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcvasreadersession/init(vascommandconfigurations:delegate:queue:)-23h52)*