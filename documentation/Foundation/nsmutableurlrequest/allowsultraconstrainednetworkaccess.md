# allowsUltraConstrainedNetworkAccess

**Framework**: Foundation  
**Kind**: property

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 26.1+
- macOS 26.1+
- tvOS 26.1+
- visionOS 26.1+
- watchOS 26.1+

## Declaration

```swift
var allowsUltraConstrainedNetworkAccess: Bool { get set }
```

#### Discussion

Sets whether a connection created with this request is allowed to use network interfaces which have been marked as ultra constrained.

NO if the receiver should not be allowed to use an interface marked as ultra constrained to satisfy the request, YES otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/allowsultraconstrainednetworkaccess)*