# timeoutDate

**Framework**: CallKit  
**Kind**: property  
**Role**: Instance Property

The time after which the action cannot be completed.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var timeoutDate: Date { get }
```

```objc
@property (nonatomic, strong, readonly) NSDate * timeoutDate;
```

## See Also

### Accessing Action Attributes
- [var uuid: UUID](./uuid.md)
  The unique identifier for the action.
- [var isComplete: Bool](./iscomplete.md)
  A Boolean value that indicates whether the action has been performed by the provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxaction/timeoutdate)*