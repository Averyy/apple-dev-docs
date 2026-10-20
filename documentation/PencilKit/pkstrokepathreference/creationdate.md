# creationDate

**Framework**: PencilKit  
**Kind**: property  
**Role**: Instance Property

The time at which this stroke path starts.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var creationDate: Date { get }
```

```objc
@property (nonatomic, readonly) NSDate * creationDate;
```

#### Discussion

The time offset of the contained stroke points is relative to this date.

## See Also

### Getting the stroke path properties
- [var count: Int](./count.md)
  The number of control points in this stroke path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepathreference/creationdate)*