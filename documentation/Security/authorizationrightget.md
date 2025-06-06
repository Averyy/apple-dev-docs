# AuthorizationRightGet(_:_:)

**Framework**: Security  
**Kind**: func

Retrieves a right definition as a dictionary.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func AuthorizationRightGet(_ rightName: UnsafePointer<CChar>, _ rightDefinition: UnsafeMutablePointer<CFDictionary?>?) -> OSStatus
```

#### Return Value

A result code. See [`Authorization Services Result Codes`](authorization-services-result-codes.md).

#### Discussion

You do not need an authorization reference to use this function because the policy database is world readable.

## Parameters

- `rightName`: An ASCII character string representing the right name. Wildcard right names are valid.
- `rightDefinition`: A reference to a dictionary. On return, this points to a dictionary of keys that define the right. Passing   checks if the right is defined. You should release the memory used by the returned dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationrightget(_:_:))*