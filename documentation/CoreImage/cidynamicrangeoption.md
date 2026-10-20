# CIDynamicRangeOption

**Framework**: Core Image  
**Kind**: struct  
**Role**: Structure

An enum string type that your code can use to select different System Tone Mapping modes.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct CIDynamicRangeOption
```

```c
typedef NSString * CIDynamicRangeOption;
```

#### Overview

These options are consistent with the analogous options available in Core Graphics, Core Animation, AppKit, UIKit, and SwiftUI, In Core Image, this option can be set on the `CISystemToneMap` filter.

## Topics

### Enumeration Cases
- [static let standard: CIDynamicRangeOption](./cidynamicrangeoption/standard.md)
  Use Standard dynamic range.
- [static let constrainedHigh: CIDynamicRangeOption](./cidynamicrangeoption/constrainedhigh.md)
  Use extended dynamic range, but brightness is modulated to optimize for co-existence with other composited content.
- [static let high: CIDynamicRangeOption](./cidynamicrangeoption/high.md)
  Use High dynamic range.
### Initializers
- [init(rawValue: String)](./cidynamicrangeoption/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidynamicrangeoption)*