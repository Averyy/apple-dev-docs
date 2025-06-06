# init(_:)

**Framework**: Network  
**Kind**: init

Initializes a port with a string.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
init?(_ service: String)
```

#### Discussion

Port strings are expected to be numeric values between 0 and 65535. Initializing with any other string will fail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwendpoint/port/init(_:))*