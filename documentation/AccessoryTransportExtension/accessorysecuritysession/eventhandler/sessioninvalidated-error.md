# sessionInvalidated(error:)

**Framework**: Accessory Transport Extension  
**Kind**: method  
**Required**: Yes

Handles session invalidation.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+
- Mac Catalyst 26.5+

## Declaration

```swift
func sessionInvalidated(error: AccessorySecuritySession.Error?)
```

#### Discussion

Clean up any stored key material when the system calls this method.

## Parameters

- `error`: An optional error that indicates the reason for invalidation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorysecuritysession/eventhandler/sessioninvalidated(error:))*