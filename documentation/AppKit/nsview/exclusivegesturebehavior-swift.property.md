# exclusiveGestureBehavior

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Declares whether gesture recognizers should be exclusive in this view and its subviews.

**Availability**:
- macOS 27.0+

## Declaration

```swift
var exclusiveGestureBehavior: NSView.ExclusiveGestureBehavior { get set }
```

```objc
@property NSViewExclusiveGestureBehavior exclusiveGestureBehavior;
```

## Mentions

- [Adopting gesture recognizers in your app](../adopting-gesture-recognizers-in-your-app.md)
- [Handling AppKit gestures](../handling-appkit-gestures.md)

## Discussion

When a view is set to `.exclusive`, and one or more of its gesture recognizers is active, a second input event will not activate any further gesture recognizers, unless that event hit tests to this view or its subviews.

Defaults to `.inherit`.

## See Also

### Managing gesture exclusivity
- [NSView.ExclusiveGestureBehavior](./exclusivegesturebehavior-swift.enum.md)
  Exclusive gesture behavior


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/exclusivegesturebehavior-swift.property)*