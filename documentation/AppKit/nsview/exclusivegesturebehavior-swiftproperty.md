# exclusiveGestureBehavior

**Framework**: AppKit  
**Kind**: property

Declares whether gesture recognizers should be exclusive in this view and its subviews.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
var exclusiveGestureBehavior: NSView.ExclusiveGestureBehavior { get set }
```

#### Discussion

When a view is set to `.exclusive`, and one or more of its gesture recognizers is active, a second input event will not activate any further gesture recognizers, unless that event hit tests to this view or its subviews.

Defaults to `.inherit`.

## See Also

- [NSView.ExclusiveGestureBehavior](nsview/exclusivegesturebehavior-swift.enum.md)
  Exclusive gesture behavior


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/exclusivegesturebehavior-swift.property)*