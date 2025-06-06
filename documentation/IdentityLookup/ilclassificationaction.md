# ILClassificationAction

**Framework**: SMS and Call Reporting  
**Kind**: enum

The actions the system can take in response to the reported communication.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
enum ILClassificationAction
```

## Topics

### Classifications
- [ILClassificationAction.none](ilclassificationaction/none.md)
  No action is required.
- [ILClassificationAction.reportJunk](ilclassificationaction/reportjunk.md)
  The system should report the communication as junk.
- [ILClassificationAction.reportJunkAndBlockSender](ilclassificationaction/reportjunkandblocksender.md)
  The system should report the communication as junk and add the number to the system’s block list.
- [ILClassificationAction.reportNotJunk](ilclassificationaction/reportnotjunk.md)
  The system should report that the communication is not junk.
### Initializers
- [init?(rawValue: Int)](ilclassificationaction/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class ILClassificationResponse](ilclassificationresponse.md)
  A response object that tells the system how to handle the reported communications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilclassificationaction)*