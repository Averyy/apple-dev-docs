# AuthorizationRightRemove(_:_:)

**Framework**: Security  
**Kind**: func

Removes a right from the policy database.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func AuthorizationRightRemove(_ authRef: AuthorizationRef, _ rightName: UnsafePointer<CChar>) -> OSStatus
```

#### Return Value

A result code. See [`Authorization Services Result Codes`](authorization-services-result-codes.md).

#### Discussion

The right you remove must be an explicit right with no wildcards. Wildcard rights are for use by system administrators for site configuration.

## Parameters

- `authRef`: A valid authorization reference used to authorize modifications.
- `rightName`: An ASCII character string representing the right name. This function does not accept wildcard right names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationrightremove(_:_:))*