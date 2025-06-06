# init(_:)

**Framework**: LightweightCodeRequirements  
**Kind**: init

Convert a [`LaunchCodeRequirement`](launchcoderequirement.md) to an [`OnDiskCodeRequirement`](ondiskcoderequirement.md) if possible.

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
init(_ launchRequirement: LaunchCodeRequirement) throws
```

#### Discussion

Conversion will fail if the [`LaunchCodeRequirement`](launchcoderequirement.md) contains a constraint that cannot be converted to [`OnDiskConstraint`](ondiskconstraint.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/ondiskcoderequirement/init(_:)-2lfey)*