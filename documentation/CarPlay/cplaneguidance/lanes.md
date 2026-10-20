# lanes

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

An array of lane objects, each describing a single lane.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
var lanes: [CPLane] { get set }
```

```objc
@property (nonatomic, copy) NSArray<CPLane *> * lanes;
```

## See Also

### Properties
- [var instructionVariants: [String]](./instructionvariants.md)
  An array of strings that represent the instruction for this lane guidance, arranged from most- to least-preferred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplaneguidance/lanes)*