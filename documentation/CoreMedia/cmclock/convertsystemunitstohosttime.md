# convertSystemUnitsToHostTime(_:)

**Framework**: Core Media  
**Kind**: method

Converts a host time from native units to a time structure.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static func convertSystemUnitsToHostTime(_ systemUnits: UInt64) -> CMTime
```

## Parameters

- `systemUnits`: The host time to convert.

## See Also

- [static func convertHostTimeToSystemUnits(CMTime) -> UInt64](cmclock/converthosttimetosystemunits(_:).md)
  Converts a host time from a time structure to the host time’s native units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmclock/convertsystemunitstohosttime(_:))*