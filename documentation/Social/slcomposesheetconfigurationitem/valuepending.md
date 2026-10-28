# valuePending

**Framework**: Social  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the configuration item’s value is ready for display.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var valuePending: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL valuePending;
```

## Discussion

Set this property to [`true`](../../Swift/true.md) if a progress indicator should be displayed, to show users that a configuration item’s value is about to display. The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Specifying Configuration Information
- [var title: String!](./title.md)
  The name of the configuration item stored as a localized string.
- [var value: String!](./value.md)
  The current value or setting of the configuration item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposesheetconfigurationitem/valuepending)*