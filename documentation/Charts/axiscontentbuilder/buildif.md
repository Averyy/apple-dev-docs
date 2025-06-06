# buildIf(_:)

**Framework**: Swift Charts  
**Kind**: method

Provides support for “if” statements in multi-statement closures, producing an optional axis content that is visible only when the condition evaluates to `true`.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static func buildIf<T>(_ content: T?) -> T? where T : AxisContent
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/axiscontentbuilder/buildif(_:))*