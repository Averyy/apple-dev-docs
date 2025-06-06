# filter(_:)

**Framework**: TabularData  
**Kind**: method  
**Required**: Yes

Returns a row grouping containing only the groups that satisfy a predicate.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+
- watchOS 8.5+

## Declaration

```swift
func filter(_ isIncluded: (DataFrame.Slice) throws -> Bool) rethrows -> Self
```

#### Return Value

A data frame slice that contains the rows that satisfy the predicate.

## Parameters

- `isIncluded`: A predicate closure that takes a group and returns a Boolean that indicates whether   the group is included.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgroupingprotocol/filter(_:))*