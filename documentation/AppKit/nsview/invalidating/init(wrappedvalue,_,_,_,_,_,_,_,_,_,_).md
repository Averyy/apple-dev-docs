# init(wrappedValue:_:_:_:_:_:_:_:_:_:_:)

**Framework**: AppKit  
**Kind**: init

Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.

**Availability**:
- macOS 12.0+
- Swift 5.1+

## Declaration

```swift
init<InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4, InvalidationType5, InvalidationType6, InvalidationType7, InvalidationType8, InvalidationType9, InvalidationType10>(wrappedValue: Value, _ invalidation1: InvalidationType1, _ invalidation2: InvalidationType2, _ invalidation3: InvalidationType3, _ invalidation4: InvalidationType4, _ invalidation5: InvalidationType5, _ invalidation6: InvalidationType6, _ invalidation7: InvalidationType7, _ invalidation8: InvalidationType8, _ invalidation9: InvalidationType9, _ invalidation10: InvalidationType10) where InvalidationType == NSView.Invalidations.Tuple<NSView.Invalidations.Tuple<NSView.Invalidations.Tuple<NSView.Invalidations.Tuple<InvalidationType1, InvalidationType2>, NSView.Invalidations.Tuple<InvalidationType3, InvalidationType4>>, NSView.Invalidations.Tuple<NSView.Invalidations.Tuple<InvalidationType5, InvalidationType6>, NSView.Invalidations.Tuple<InvalidationType7, InvalidationType8>>>, NSView.Invalidations.Tuple<InvalidationType9, InvalidationType10>>, InvalidationType1 : NSViewInvalidating, InvalidationType2 : NSViewInvalidating, InvalidationType3 : NSViewInvalidating, InvalidationType4 : NSViewInvalidating, InvalidationType5 : NSViewInvalidating, InvalidationType6 : NSViewInvalidating, InvalidationType7 : NSViewInvalidating, InvalidationType8 : NSViewInvalidating, InvalidationType9 : NSViewInvalidating, InvalidationType10 : NSViewInvalidating
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/invalidating/init(wrappedvalue:_:_:_:_:_:_:_:_:_:_:))*