# isComplete

**Framework**: CallKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the action has been performed by the provider.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var isComplete: Bool { get }
```

```objc
@property (nonatomic, assign, readonly, getter=isComplete) BOOL complete;
```

#### Discussion

This property is initialized to [`false`](../../Swift/false.md), and is set to [`true`](../../Swift/true.md) when either the [`fulfill()`](./fulfill%28%29.md) or [`fail()`](./fail%28%29.md) method is called.

#### See also

##### Related Documentation

- [`fulfill()`](./fulfill%28%29.md)
- [`fail()`](./fail%28%29.md)

## See Also

### Accessing Action Attributes
- [var uuid: UUID](./uuid.md)
  The unique identifier for the action.
- [var timeoutDate: Date](./timeoutdate.md)
  The time after which the action cannot be completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxaction/iscomplete)*