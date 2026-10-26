# adjustmentTimestamp

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The date when the asset was last edited.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var adjustmentTimestamp: Date? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) NSDate * adjustmentTimestamp;
```

#### Discussion

If the asset has never been edited, then this property is nil. If the asset was edited and later reverted, such that hasAdjustments is false, then `adjustmentTimestamp` is the timestamp of the revert operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phasset/adjustmenttimestamp)*