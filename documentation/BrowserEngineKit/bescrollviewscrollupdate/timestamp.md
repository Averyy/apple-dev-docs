# timestamp

**Framework**: BrowserEngineKit  
**Kind**: property  
**Role**: Instance Property

The time at which a scroll update occurs.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var timestamp: TimeInterval { get }
```

```objc
@property (nonatomic, readonly) NSTimeInterval timestamp;
```

## See Also

### Retrieving scroll state information
- [var phase: BEScrollViewScrollUpdate.Phase](./phase-swift.property.md)
  A value that indicates the scroll update’s position in the scrolling life cycle.
- [BEScrollViewScrollUpdate.Phase](./phase-swift.enum.md)
  Phases in the scroll gesture life cycle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bescrollviewscrollupdate/timestamp)*