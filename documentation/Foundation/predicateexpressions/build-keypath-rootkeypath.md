# build_KeyPath(root:keyPath:)

**Framework**: Foundation  
**Kind**: method

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static func build_KeyPath<Root, Value>(root: Root, keyPath: any KeyPath<Root.Output, Value> & Sendable) -> PredicateExpressions.KeyPath<Root, Value> where Root : PredicateExpression
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/build_keypath(root:keypath:))*