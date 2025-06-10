# NSView.Invalidating

**Framework**: AppKit  
**Kind**: struct

A property wrapper that notifies the system that a property value change has invalidated an aspect of the containing view.

**Availability**:
- macOS 12.0+
- Swift 5.1+

## Declaration

```swift
@propertyWrapper
struct Invalidating<Value, InvalidationType> where Value : Equatable, InvalidationType : NSViewInvalidating
```

#### Overview

Use this wrapper when a change in the property value invalidates the display, layout, configuration, constraints, or intrinsic sizing of a view. This wrapper performs any actions necessary to notify the system that your view is invalid and requires an update. The actions depend on the invalidation types you specify. For more information on available invalidation types, see [`NSViewInvalidating`](nsviewinvalidating.md).

The following example uses the [`NSView.Invalidating`](nsview/invalidating.md) wrapper with the `display` type on the property `fillColor` and the `display` and `layout` type on the property `badgePosition`.

```swift
class MyView: NSView {
    @Invalidating(.display) var fillColor: NSColor
    
    @Invalidating(.display, .layout) var badgePosition: NSRectEdge
}
```

When you change the fill color, the property wrapper sets [`needsDisplay`](nsview/needsdisplay.md) to true, causing the system to redraw the view. When you change the badge position, the property wrapper also sets [`needsLayout`](nsview/needslayout.md) to true, causing the system to update the view’s subviews before it redraws.

Functions such as `setNeedsDisplay` and `setNeedsLayout` perform changes on the next update cycle. You can make changes to multiple properties and views before any of those views update. Consolidating the updates to one update cycle is usually better for performance.

> **Note**:  You only use `NSView.Invalidating` on subclasses of `NSView`.

## Topics

### Creating an Invalidating Property Wrapper
- [init(wrappedValue: Value, InvalidationType)](nsview/invalidating/init(wrappedvalue:_:).md)
  Creates a property wrapper that notifies the system when a change in the property value invalidates an aspect of the containing view.
- [init<InvalidationType1, InvalidationType2>(wrappedValue: Value, InvalidationType1, InvalidationType2)](nsview/invalidating/init(wrappedvalue:_:_:).md)
  Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init<InvalidationType1, InvalidationType2, InvalidationType3>(wrappedValue: Value, InvalidationType1, InvalidationType2, InvalidationType3)](nsview/invalidating/init(wrappedvalue:_:_:_:).md)
  Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init<InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4>(wrappedValue: Value, InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4)](nsview/invalidating/init(wrappedvalue:_:_:_:_:).md)
  Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init<InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4, InvalidationType5>(wrappedValue: Value, InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4, InvalidationType5)](nsview/invalidating/init(wrappedvalue:_:_:_:_:_:).md)
  Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init<InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4, InvalidationType5, InvalidationType6>(wrappedValue: Value, InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4, InvalidationType5, InvalidationType6)](nsview/invalidating/init(wrappedvalue:_:_:_:_:_:_:).md)
  Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init<InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4, InvalidationType5, InvalidationType6, InvalidationType7>(wrappedValue: Value, InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4, InvalidationType5, InvalidationType6, InvalidationType7)](nsview/invalidating/init(wrappedvalue:_:_:_:_:_:_:_:).md)
  Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init<InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4, InvalidationType5, InvalidationType6, InvalidationType7, InvalidationType8>(wrappedValue: Value, InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4, InvalidationType5, InvalidationType6, InvalidationType7, InvalidationType8)](nsview/invalidating/init(wrappedvalue:_:_:_:_:_:_:_:_:).md)
  Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init<InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4, InvalidationType5, InvalidationType6, InvalidationType7, InvalidationType8, InvalidationType9>(wrappedValue: Value, InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4, InvalidationType5, InvalidationType6, InvalidationType7, InvalidationType8, InvalidationType9)](nsview/invalidating/init(wrappedvalue:_:_:_:_:_:_:_:_:_:).md)
  Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init<InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4, InvalidationType5, InvalidationType6, InvalidationType7, InvalidationType8, InvalidationType9, InvalidationType10>(wrappedValue: Value, InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4, InvalidationType5, InvalidationType6, InvalidationType7, InvalidationType8, InvalidationType9, InvalidationType10)](nsview/invalidating/init(wrappedvalue:_:_:_:_:_:_:_:_:_:_:).md)
  Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.

## See Also

- [protocol NSViewInvalidating](nsviewinvalidating.md)
  Implements a type of invalidation that can occur on a view that requires an update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/invalidating)*