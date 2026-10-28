# segmentCount

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The number of segments in the segmented control.

**Availability**:
- macOS

## Declaration

```swift
var segmentCount: Int { get set }
```

```objc
@property NSInteger segmentCount;
```

## Discussion

This property contains the number of segments the segmented control should have. If this value is less than the number of segments currently in the control, segments are removed from the right of the control. Similarly, if the number is greater than the current number of segments, the new segments are added on the right. This value must be between `0` and `2049`.

## See Also

### Related Documentation
- [Segmented Control Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SegmentedControl/SegmentedControl.html#//apple_ref/doc/uid/10000182i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcell/segmentcount)*