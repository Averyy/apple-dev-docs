# observedProgress

**Framework**: AppKit  
**Kind**: property

The progress object to use for updating the progress view.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
var observedProgress: Progress? { get set }
```

#### Discussion

Set this property when you want the progress view to automatically update its progress value using the information it receives from the [`Progress`](https://developer.apple.com/documentation/Foundation/Progress) object. Setting this property also modifies the [`isIndeterminate`](nsprogressindicator/isindeterminate.md), [`minValue`](nsprogressindicator/minvalue.md), [`maxValue`](nsprogressindicator/maxvalue.md), and [`doubleValue`](nsprogressindicator/doublevalue.md) properties of the indicator. Set the property to `nil` when you want to update the progress manually. The default value of this property is `nil`.

For more information on configuring a progress object, see [`Progress`](https://developer.apple.com/documentation/Foundation/Progress).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprogressindicator/observedprogress)*