# convertHostTimeToSystemUnits(_:)

**Framework**: Core Media  
**Kind**: method

Converts a host time from a time structure to the host time’s native units.

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
static func convertHostTimeToSystemUnits(_ hostTime: CMTime) -> UInt64
```

## Parameters

- `hostTime`: The host time to convert.

## See Also

- [static func convertSystemUnitsToHostTime(UInt64) -> CMTime](cmclock/convertsystemunitstohosttime(_:).md)
  Converts a host time from native units to a time structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmclock/converthosttimetosystemunits(_:))*