# subscript(dynamicMember:)

**Framework**: SwiftUI  
**Kind**: subscript

Access the value of the attribute to constrain.

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
subscript(dynamicMember keyPath: KeyPath<Subscope, Attribute>) -> Attribute.Value? { get set }
```

#### Overview

For details on how attribute value constraining works, refer to [`constrain(_:)`](attributedtextvalueconstraint/constrain(_:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextformatting/attributecontainerproxy/scoped/subscript(dynamicmember:))*