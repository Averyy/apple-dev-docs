# UIPopoverBackgroundViewMethods

**Framework**: UIKit  
**Kind**: protocol

A set of methods that popover background view subclasses must implement.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol UIPopoverBackgroundViewMethods
```

#### Overview

The methods in this protocol are called only once when the popover is presented. All methods of this protocol are required.

## Topics

### Returning the content view insets
- [static func contentViewInsets() -> UIEdgeInsets](uipopoverbackgroundviewmethods/contentviewinsets.md)
  The insets for the content portion of the popover.
### Accessing the arrow metrics
- [static func arrowBase() -> CGFloat](uipopoverbackgroundviewmethods/arrowbase.md)
  The width of the arrow triangle at its base.
- [static func arrowHeight() -> CGFloat](uipopoverbackgroundviewmethods/arrowheight.md)
  The height of the arrow (measured in points) from its base to its tip.

## Relationships

### Conforming Types
- [UIPopoverBackgroundView](uipopoverbackgroundview.md)

## See Also

- [Displaying transient content in a popover](displaying-transient-content-in-a-popover.md)
  Show a temporary interface on top of your app’s content on iPad.
- [class UIPopoverPresentationController](uipopoverpresentationcontroller.md)
  An object that manages the display of content in a popover.
- [class UIPopoverBackgroundView](uipopoverbackgroundview.md)
  The background appearance for a popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopoverbackgroundviewmethods)*