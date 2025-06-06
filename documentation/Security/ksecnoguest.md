# kSecNoGuest

**Framework**: Security  
**Kind**: var

Not a valid `SecGuestRef` object.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var kSecNoGuest: SecGuestRef { get }
```

#### Discussion

Some functions in the API use this value to indicate that there is no guest, and some functions use it to indicate that the function applies to the host itself rather than to a guest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecnoguest)*