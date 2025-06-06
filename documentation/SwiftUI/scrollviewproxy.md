# ScrollViewProxy

**Framework**: SwiftUI  
**Kind**: struct

A proxy value that supports programmatic scrolling of the scrollable views within a view hierarchy.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
struct ScrollViewProxy
```

#### Overview

You don’t create instances of `ScrollViewProxy` directly. Instead, your [`ScrollViewReader`](scrollviewreader.md) receives an instance of `ScrollViewProxy` in its `content` view builder. You use actions within this view builder, such as button and gesture handlers or the [`onChange(of:perform:)`](view/onchange(of:perform:).md) method, to call the proxy’s [`scrollTo(_:anchor:)`](scrollviewproxy/scrollto(_:anchor:).md) method.

## Topics

### Performing scrolling
- [func scrollTo<ID>(ID, anchor: UnitPoint?)](scrollviewproxy/scrollto(_:anchor:).md)
  Scans all scroll views contained by the proxy for the first with a child view with identifier `id`, and then scrolls to that view.

## See Also

- [struct ScrollView](scrollview.md)
  A scrollable view.
- [struct ScrollViewReader](scrollviewreader.md)
  A view that provides programmatic scrolling, by working with a proxy to scroll to known child views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrollviewproxy)*