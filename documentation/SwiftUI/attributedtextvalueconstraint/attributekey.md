# AttributeKey

**Framework**: SwiftUI  
**Kind**: associatedtype  
**Required**: Yes

The attribute constrained by this constraint.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
associatedtype AttributeKey : AttributedStringKey where Self.AttributeKey.Value : Sendable
```

#### Discussion

> **Note**: This attribute must always be part of the associated `Scope`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextvalueconstraint/attributekey)*