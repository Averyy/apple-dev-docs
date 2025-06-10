# AttributeKey

**Framework**: SwiftUI  
**Kind**: associatedtype  
**Required**: Yes

The attribute constrained by this constraint.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
associatedtype AttributeKey : AttributedStringKey where Self.AttributeKey.Value : Sendable
```

#### Discussion

> **Note**: This attribute must always be part of the associated `Scope`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextvalueconstraint/attributekey)*