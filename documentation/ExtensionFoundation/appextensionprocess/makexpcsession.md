# makeXPCSession()

**Framework**: ExtensionFoundation  
**Kind**: method

Creates a new XPC session to the extension process.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
func makeXPCSession() throws -> XPCSession
```

#### Return Value

The session object representing the created XPC connection.

#### Discussion

This method creates an inactive XPCSession to the extension process and returns it. You’re responsible for configuring and activating the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionprocess/makexpcsession())*