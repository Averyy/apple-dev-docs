# valuePending

**Framework**: Social  
**Kind**: property

A Boolean value that indicates whether the configuration item’s value is ready for display.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var valuePending: Bool { get set }
```

#### Discussion

Set this property to [`true`](https://developer.apple.com/documentation/swift/true) if a progress indicator should be displayed, to show users that a configuration item’s value is about to display. The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var title: String!](slcomposesheetconfigurationitem/title.md)
  The name of the configuration item stored as a localized string.
- [var value: String!](slcomposesheetconfigurationitem/value.md)
  The current value or setting of the configuration item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposesheetconfigurationitem/valuepending)*