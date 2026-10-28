# instructionVariants

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

An array of instruction variants for the maneuver.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var instructionVariants: [String] { get set }
```

```objc
@property (nonatomic, copy) NSArray<NSString *> * instructionVariants;
```

## Discussion

Localize each variant for display to the user, and make sure the array contains at least one variant. The system displays the first variant that fits into the available screen space, so arrange the variants in order from most- to least-preferred.

> **Note**:  If you provide both [`instructionVariants`](./instructionvariants.md) and [`attributedInstructionVariants`](./attributedinstructionvariants.md), the system displays instructions from the attributed instruction variants array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaneuver/instructionvariants)*