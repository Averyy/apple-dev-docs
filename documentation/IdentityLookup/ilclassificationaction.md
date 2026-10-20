# ILClassificationAction

**Framework**: SMS and Call Reporting  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum ILClassificationAction : NSInteger;
```

## Topics

### Classifications
- [ILClassificationAction.none](./ilclassificationaction/none.md)
  No action is required.
- [ILClassificationAction.reportJunk](./ilclassificationaction/reportjunk.md)
  The system should report the communication as junk.
- [ILClassificationAction.reportJunkAndBlockSender](./ilclassificationaction/reportjunkandblocksender.md)
  The system should report the communication as junk and add the number to the system’s block list.
- [ILClassificationAction.reportNotJunk](./ilclassificationaction/reportnotjunk.md)
  The system should report that the communication is not junk.
### Initializers
- [init?(rawValue: Int)](./ilclassificationaction/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Responses
- [class ILClassificationResponse](./ilclassificationresponse.md)
  A response object that tells the system how to handle the reported communications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilclassificationaction)*