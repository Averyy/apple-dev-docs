# init(_:)

**Framework**: LightweightCodeRequirements  
**Kind**: init

Convert a [`OnDiskCodeRequirement`](ondiskcoderequirement.md) to a [`LaunchCodeRequirement`](launchcoderequirement.md) if possible.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
init(_ onDiskRequirement: OnDiskCodeRequirement) throws
```

#### Discussion

Conversion will fail if the [`OnDiskCodeRequirement`](ondiskcoderequirement.md) contains a constraint that cannot be converted to [`LaunchConstraint`](launchconstraint.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/launchcoderequirement/init(_:)-6hixy)*