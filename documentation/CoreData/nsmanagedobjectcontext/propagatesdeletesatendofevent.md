# propagatesDeletesAtEndOfEvent

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the context propagates deletes at the end of the event in which a change was made.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var propagatesDeletesAtEndOfEvent: Bool { get set }
```

```objc
@property (nonatomic) BOOL propagatesDeletesAtEndOfEvent;
```

## Discussion

[`true`](../../Swift/true.md) if the receiver propagates deletes at the end of the event in which a change was made, [`false`](../../Swift/false.md) if it propagates deletes only during a save operation. The default is [`true`](../../Swift/true.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/propagatesdeletesatendofevent)*