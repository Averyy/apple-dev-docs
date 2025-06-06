# build_ForcedUnwrap(_:)

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
static func build_ForcedUnwrap<Inner, Wrapped>(_ inner: Inner) -> PredicateExpressions.ForcedUnwrap<Inner, Wrapped> where Inner : PredicateExpression, Inner.Output == Wrapped?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/build_forcedunwrap(_:))*