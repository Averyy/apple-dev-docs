# init(rawValue:)

**Framework**: Foundation  
**Kind**: init

Creates an HTTP cookie string policy from the given raw string.

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
init(rawValue: String)
```

#### Discussion

URL Loading System ignores any policy with a raw value other than the predefined policy values: `strict` and `lax`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookiestringpolicy/init(rawvalue:))*