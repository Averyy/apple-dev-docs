# hostName

**Framework**: Foundation  
**Kind**: property

A string containing the DNS hostname for this service.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var hostName: String? { get }
```

#### Discussion

This value is `nil` until the service has been resolved (when `addresses` is non-`nil`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice/hostname)*