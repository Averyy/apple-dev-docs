# validate(snapshot:)

**Framework**: TabletopKit  
**Kind**: method  
**Required**: Yes

Implement this function to detect whether the action is valid and should be applied given the state of the table represented by `snapshot`. If not implemented, the action is always considered valid. It is important that the validation for a given action is only a function of the given snapshot and the data of the action instance.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
func validate(snapshot: TableSnapshot) -> Bool
```

## Parameters

- `snapshot`: The state of the table to be used for this validation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/customaction/validate(snapshot:))*