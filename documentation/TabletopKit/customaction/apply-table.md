# apply(table:)

**Framework**: TabletopKit  
**Kind**: method  
**Required**: Yes

Implement this function to perform the changes to the table state that this action represents. It is important that the code performed in this function is only a function of the provided table state and the data of the action instance.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
func apply(table: inout TableState)
```

## Parameters

- `table`: The table to modify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/customaction/apply(table:))*