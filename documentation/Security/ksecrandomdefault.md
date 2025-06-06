# kSecRandomDefault

**Framework**: Security  
**Kind**: var

An alias for the default random number generator.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kSecRandomDefault: SecRandomRef
```

#### Discussion

When passed to the [`SecRandomCopyBytes(_:_:_:)`](secrandomcopybytes(_:_:_:).md) function as the random number generator reference, this constant indicates that the default number generator should be used.

This constant is a synonym for `NULL`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecrandomdefault)*