# stepRate

**Framework**: Metal  
**Kind**: property

How frequently the step function should load data.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var stepRate: Int { get set }
```

#### Discussion

The interpretation of this value depends on the setting of `stepFunction`.

## See Also

- [var stride: Int](mtlbufferlayoutdescriptor/stride.md)
  The number of bytes from one buffer entry to the next.
- [var stepFunction: MTLStepFunction](mtlbufferlayoutdescriptor/stepfunction.md)
  Determines how and when compute functions fetch data.
- [enum MTLStepFunction](mtlstepfunction.md)
  The frequency and locations at which a function fetches attribute data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbufferlayoutdescriptor/steprate)*