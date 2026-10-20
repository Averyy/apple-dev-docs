# RosterRequest

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Object

The request for a list of classes.

**Availability**:
- Device Assignment Services 5.0+

## Declaration

```
object RosterRequest
```

## Properties

- `cursor` (string): A hex string that represents the starting position for a request. This is used for pagination. On the initial request, this should be omitted.
- `limit` (int32): The maximum number of entries to return.

  **Default**: `1000`; **Maximum**: `1000`

## See Also

### Request and Response
- [object RosterClassResponse](./rosterclassresponse.md)
  The response that contains a list of classes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/rosterrequest)*