# uuid

**Framework**: CallKit  
**Kind**: property  
**Role**: Instance Property

The unique identifier for the action.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var uuid: UUID { get }
```

```objc
@property (nonatomic, copy, readonly) NSUUID * UUID;
```

## See Also

### Accessing Action Attributes
- [var isComplete: Bool](./iscomplete.md)
  A Boolean value that indicates whether the action has been performed by the provider.
- [var timeoutDate: Date](./timeoutdate.md)
  The time after which the action cannot be completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxaction/uuid)*