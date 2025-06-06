# stride

**Framework**: Metal  
**Kind**: property

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

#### Discussion

The default value is `1`. See [`Metal feature set tables (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for `stride` alignment restrictions on GPU architectures.

## See Also

- [var stepFunction: MTLStepFunction](mtlbufferlayoutdescriptor/stepfunction.md)
  Determines how and when compute functions fetch data.
- [var stepRate: Int](mtlbufferlayoutdescriptor/steprate.md)
  How frequently the step function should load data.
- [enum MTLStepFunction](mtlstepfunction.md)
  The frequency and locations at which a function fetches attribute data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbufferlayoutdescriptor/stride)*