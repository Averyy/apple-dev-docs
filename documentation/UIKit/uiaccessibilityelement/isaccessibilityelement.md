# isAccessibilityElement

**Framework**: UIKit  
**Kind**: property

A Boolean value indicating whether the item is an accessibility element an assistive application can access.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isAccessibilityElement: Bool { get set }
```

#### Discussion

The default value for this property is [`false`](https://developer.apple.com/documentation/swift/false). If the receiver is a UIKit control, the default value is [`true`](https://developer.apple.com/documentation/swift/true).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilityelement/isaccessibilityelement)*