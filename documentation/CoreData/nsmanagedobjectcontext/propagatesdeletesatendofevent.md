# propagatesDeletesAtEndOfEvent

**Framework**: Core Data  
**Kind**: property

A Boolean value that indicates whether the context propagates deletes at the end of the event in which a change was made.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var propagatesDeletesAtEndOfEvent: Bool { get set }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if the receiver propagates deletes at the end of the event in which a change was made, [`false`](https://developer.apple.com/documentation/swift/false) if it propagates deletes only during a save operation. The default is [`true`](https://developer.apple.com/documentation/swift/true).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/propagatesdeletesatendofevent)*