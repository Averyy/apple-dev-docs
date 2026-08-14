# init(views:)

**Framework**: AppKit  
**Kind**: init

Creates and returns a stack view with a specified array of views.

**Availability**:
- macOS 10.9+

## Declaration

```swift
convenience init(views: [NSView])
```

#### Return Value

A stack view initialized with the specified array of views.

#### Discussion

The returned stack view has horizontal layout direction and its [`translatesAutoresizingMaskIntoConstraints`](nsview/translatesautoresizingmaskintoconstraints.md) property is set to the Boolean value [`false`](https://developer.apple.com/documentation/swift/false). The views you provide in the `views` parameter are placed into the stack view’s leading gravity area.

## Parameters

- `views`: The array of views for the new stack view.

## See Also

- [View Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaViewsGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40002978)
- [class NSLayoutConstraint](nslayoutconstraint.md)
  The relationship between two user interface objects that must be satisfied by the constraint-based layout system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/init(views:))*