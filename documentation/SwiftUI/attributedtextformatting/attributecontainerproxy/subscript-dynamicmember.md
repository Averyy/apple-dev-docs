# subscript(dynamicMember:)

**Framework**: SwiftUI  
**Kind**: subscript

Access the value of the attribute to constrain.

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
subscript(dynamicMember keyPath: KeyPath<AttributeDynamicLookup, Attribute>) -> Attribute.Value? { get set }
```

#### Overview

For details on how attribute value constraining works, refer to [`constrain(_:)`](attributedtextvalueconstraint/constrain(_:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextformatting/attributecontainerproxy/subscript(dynamicmember:))*