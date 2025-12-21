# supportsSecureCoding

**Framework**: Foundation  
**Kind**: property  
**Required**: Yes

A Boolean value that indicates whether or not the class supports secure coding.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var supportsSecureCoding: Bool { get }
```

#### Discussion

When you write a class that supports secure coding, ensure that this class property’s getter returns [`true`](https://developer.apple.com/documentation/Swift/true).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssecurecoding/supportssecurecoding)*