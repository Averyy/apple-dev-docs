# observedProgress

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The progress object to use for updating the progress view.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var observedProgress: Progress? { get set }
```

```objc
@property (strong, nullable) NSProgress * observedProgress;
```

## Discussion

Set this property when you want the progress view to automatically update its progress value using the information it receives from the [`Progress`](../../Foundation/progress.md) object. Setting this property also modifies the [`isIndeterminate`](./isindeterminate.md), [`minValue`](./minvalue.md), [`maxValue`](./maxvalue.md), and [`doubleValue`](./doublevalue.md) properties of the indicator. Set the property to `nil` when you want to update the progress manually. The default value of this property is `nil`.

For more information on configuring a progress object, see [`Progress`](../../Foundation/progress.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprogressindicator/observedprogress)*