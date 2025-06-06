# mapGroups(_:)

**Framework**: TabularData  
**Kind**: method  
**Required**: Yes

Generates a row grouping that applies a transformation closure to each group in the original.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func mapGroups(_ transform: (DataFrame.Slice) throws -> DataFrame) rethrows -> Self
```

## Parameters

- `transform`: A closure that generates a data frame from a data frame slice that represents a group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgroupingprotocol/mapgroups(_:))*