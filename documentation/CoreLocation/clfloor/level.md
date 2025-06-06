# level

**Framework**: Core Location  
**Kind**: property

The logical floor of the building.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var level: Int { get }
```

#### Discussion

Level values represent logical levels above or below ground level and are not intended to correspond to any numbering scheme in use by the building itself. The ground floor of a building is always represented by the value `0`. Floors above the ground floor are represented by positive integers, so a value of `1` represents the floor above ground level, a value of `2` represents two floors above ground level, and so on. Floors below the ground floor are represented by corresponding negative integers, with a value of -1 representing the floor immediately below ground level and so on.

It is erroneous to use the user’s level in a building as an estimate of altitude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clfloor/level)*