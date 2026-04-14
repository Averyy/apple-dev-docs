# messageReceived(_:completion:)

**Framework**: Accessory Transport Extension  
**Kind**: method  
**Required**: Yes

Security message received.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
func messageReceived(_ message: SecurityMessage, completion: @escaping @Sendable (AccessoryMessage.Result) -> Void)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorysecuritysession/eventhandler/messagereceived(_:completion:))*