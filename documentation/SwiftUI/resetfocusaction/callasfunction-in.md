# callAsFunction(in:)

**Framework**: SwiftUI  
**Kind**: method

Asks the focus sytem to reevaluate the default focus item.

**Availability**:
- macOS 12.0+
- tvOS 14.0+
- watchOS 7.0+

## Declaration

```swift
func callAsFunction(in namespace: Namespace.ID)
```

#### Discussion

The focus system reevaluates default focus when the currently-focused item is within the provided namespace.

## Parameters

- `namespace`: The namespace inside which SwiftUI should   reevaluate default focus. The namespace should match the    block where focus requires reevaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/resetfocusaction/callasfunction(in:))*