# isEnabled

**Framework**: UIKit  
**Kind**: property

A Boolean value indicating whether the action is currently enabled.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isEnabled: Bool { get set }
```

#### Discussion

The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true). Changing the value to [`false`](https://developer.apple.com/documentation/swift/false) causes the action to appear dimmed in the resulting alert. When an action is disabled, taps on the corresponding button have no effect.

## See Also

- [var title: String?](uialertaction/title.md)
  The title of the action’s button.
- [var style: UIAlertAction.Style](uialertaction/style-swift.property.md)
  The style that applies to the action’s button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertaction/isenabled)*