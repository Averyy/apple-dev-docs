# stepFunction

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

Determines how and when compute functions fetch data.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var stepFunction: MTLStepFunction { get set }
```

```objc
@property (nonatomic, assign) MTLStepFunction stepFunction;
```

## See Also

### Describing fetch behavior
- [var stride: Int](./stride.md)
  The number of bytes from one buffer entry to the next.
- [var stepRate: Int](./steprate.md)
  How frequently the step function should load data.
- [enum MTLStepFunction](../mtlstepfunction.md)
  The frequency and locations at which a function fetches attribute data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbufferlayoutdescriptor/stepfunction)*