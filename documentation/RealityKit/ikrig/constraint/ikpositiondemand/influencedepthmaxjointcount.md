# influenceDepthMaxJointCount

**Framework**: RealityKit  
**Kind**: property

The number of joints to be influenced by this demand.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
var influenceDepthMaxJointCount: Int
```

#### Discussion

The count starts from the constrained joint and continues up the chain to the skeleton’s root.

> **Note**: A depth of `0` disables the constraint, while negative values are treated as `Int.max`


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikrig/constraint/ikpositiondemand/influencedepthmaxjointcount)*