# address

**Framework**: Core Foundation  
**Kind**: property

A CFData object holding the contents of a `struct sockaddr` appropriate for the given protocol family (`struct sockaddr_in` or `struct sockaddr_in6`, for example), identifying the address of the socket.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var address: Unmanaged<CFData>!
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsocketsignature/address)*