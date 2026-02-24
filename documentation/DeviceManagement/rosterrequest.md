# RosterRequest

**Framework**: Device Management  
**Kind**: dictionary

The request for a list of classes.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object RosterRequest
```

## Properties

- `cursor` (string): A hex string that represents the starting position for a request. This is used for pagination. On the initial request, this should be omitted.
- `limit` (int32): The maximum number of entries to return.

## See Also

- [object RosterClassResponse](rosterclassresponse.md)
  The response that contains a list of classes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/rosterrequest)*