# hostName

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A string containing the DNS hostname for this service.

**Availability**:
- iOS 2.0+ - Deprecated in 27.2
- iPadOS 2.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.2+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use nw_connection_t or nw_listener_t in Network framework instead

## Declaration

```swift
var hostName: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * hostName;
```

## Discussion

This value is `nil` until the service has been resolved (when `addresses` is non-`nil`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice/hostname)*