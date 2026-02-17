# cancel(error:)

**Framework**: Accessory Transport Extension  
**Kind**: method

Cancels the security session.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)

## Declaration

```swift
func cancel(error: (any Error)?)
```

## Parameters

- `error`: An optional error that indicates the reason for cancellation.

## See Also

- [func sendSecurityEvent(AccessorySecurity.Event) throws](accessorysecuritysession/sendsecurityevent(_:).md)
  Sends a security event to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorysecuritysession/cancel(error:))*