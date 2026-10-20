# stride

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The number of bytes from one buffer entry to the next.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var stride: Int { get set }
```

```objc
@property (nonatomic, assign) NSUInteger stride;
```

#### Discussion

The default value is `1`. Check the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for potential alignment restrictions.

## See Also

### Describing fetch behavior
- [var stepFunction: MTLStepFunction](./stepfunction.md)
  Determines how and when compute functions fetch data.
- [var stepRate: Int](./steprate.md)
  How frequently the step function should load data.
- [enum MTLStepFunction](../mtlstepfunction.md)
  The frequency and locations at which a function fetches attribute data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbufferlayoutdescriptor/stride)*