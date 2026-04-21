# sessionInvalidated(error:)

**Framework**: Accessory Transport Extension  
**Kind**: method  
**Required**: Yes

Handles session invalidation.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)
- Mac Catalyst 26.5+ (Beta)

## Declaration

```swift
func sessionInvalidated(error: AccessoryTransportSession.Error?)
```

#### Discussion

Clean up connection state and resources when the system calls this method.

## Parameters

- `error`: An optional error that indicates the reason for invalidation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/eventhandler/sessioninvalidated(error:))*