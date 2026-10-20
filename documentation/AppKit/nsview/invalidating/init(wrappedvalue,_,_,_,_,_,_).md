# init(wrappedValue:_:_:_:_:_:_:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.

**Availability**:
- macOS 12.0+
- Swift 5.1+

## Declaration

```swift
init<InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4, InvalidationType5, InvalidationType6>(wrappedValue: Value, _ invalidation1: InvalidationType1, _ invalidation2: InvalidationType2, _ invalidation3: InvalidationType3, _ invalidation4: InvalidationType4, _ invalidation5: InvalidationType5, _ invalidation6: InvalidationType6) where InvalidationType == NSView.Invalidations.Tuple<NSView.Invalidations.Tuple<NSView.Invalidations.Tuple<InvalidationType1, InvalidationType2>, NSView.Invalidations.Tuple<InvalidationType3, InvalidationType4>>, NSView.Invalidations.Tuple<InvalidationType5, InvalidationType6>>, InvalidationType1 : NSViewInvalidating, InvalidationType2 : NSViewInvalidating, InvalidationType3 : NSViewInvalidating, InvalidationType4 : NSViewInvalidating, InvalidationType5 : NSViewInvalidating, InvalidationType6 : NSViewInvalidating
```

## Parameters

- `wrappedValue`: The underlying value referenced by the invalidating variable.
- `invalidation1`: A type of invalidation.
- `invalidation2`: A type of invalidation.
- `invalidation3`: A type of invalidation.
- `invalidation4`: A type of invalidation.
- `invalidation5`: A type of invalidation.
- `invalidation6`: A type of invalidation.

## See Also

### Creating an Invalidating Property Wrapper
- [init(wrappedValue: Value, InvalidationType)](./init%28wrappedvalue,_%29.md)
  Creates a property wrapper that notifies the system when a change in the property value invalidates an aspect of the containing view.
- [init<InvalidationType1, InvalidationType2>(wrappedValue: Value, InvalidationType1, InvalidationType2)](./init%28wrappedvalue,_,_%29.md)
  Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init<InvalidationType1, InvalidationType2, InvalidationType3>(wrappedValue: Value, InvalidationType1, InvalidationType2, InvalidationType3)](./init%28wrappedvalue,_,_,_%29.md)
  Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init<InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4>(wrappedValue: Value, InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4)](./init%28wrappedvalue,_,_,_,_%29.md)
  Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init<InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4, InvalidationType5>(wrappedValue: Value, InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4, InvalidationType5)](./init%28wrappedvalue,_,_,_,_,_%29.md)
  Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init<InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4, InvalidationType5, InvalidationType6, InvalidationType7>(wrappedValue: Value, InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4, InvalidationType5, InvalidationType6, InvalidationType7)](./init%28wrappedvalue,_,_,_,_,_,_,_%29.md)
  Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init<InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4, InvalidationType5, InvalidationType6, InvalidationType7, InvalidationType8>(wrappedValue: Value, InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4, InvalidationType5, InvalidationType6, InvalidationType7, InvalidationType8)](./init%28wrappedvalue,_,_,_,_,_,_,_,_%29.md)
  Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init<InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4, InvalidationType5, InvalidationType6, InvalidationType7, InvalidationType8, InvalidationType9>(wrappedValue: Value, InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4, InvalidationType5, InvalidationType6, InvalidationType7, InvalidationType8, InvalidationType9)](./init%28wrappedvalue,_,_,_,_,_,_,_,_,_%29.md)
  Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init<InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4, InvalidationType5, InvalidationType6, InvalidationType7, InvalidationType8, InvalidationType9, InvalidationType10>(wrappedValue: Value, InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4, InvalidationType5, InvalidationType6, InvalidationType7, InvalidationType8, InvalidationType9, InvalidationType10)](./init%28wrappedvalue,_,_,_,_,_,_,_,_,_,_%29.md)
  Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/invalidating/init(wrappedvalue:_:_:_:_:_:_:))*