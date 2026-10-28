# summary(of:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Generates a categorical summary of the columns you select by name.

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
func summary(of columnNames: String...) -> any GroupSummaries
```

## Return Value

A [`GroupSummaries`](../groupsummaries.md) instance that contains categorical summary of the columns you select.

## Parameters

- `columnNames`: A comma-separated, or variadic, list of column names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgroupingprotocol/summary(of:)-n5ia)*