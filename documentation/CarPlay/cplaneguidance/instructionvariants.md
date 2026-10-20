# instructionVariants

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

An array of strings that represent the instruction for this lane guidance, arranged from most- to least-preferred.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
var instructionVariants: [String] { get set }
```

```objc
@property (nonatomic, copy) NSArray<NSString *> * instructionVariants;
```

#### Discussion

You need to provide at least one variant. Provide the variant strings as localized, displayable content.

## See Also

### Properties
- [var lanes: [CPLane]](./lanes.md)
  An array of lane objects, each describing a single lane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplaneguidance/instructionvariants)*