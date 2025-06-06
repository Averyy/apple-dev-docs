# identifier

**Framework**: UIKit  
**Kind**: property

A string used to identify the layout guide.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var identifier: String { get set }
```

#### Discussion

By default, the `identifier` property is an empty string. Assign a nonempty string to identify this layout guide. This string appears as part of the guide’s description when the guide is printed to the console. You can also use the identifier to find a particular layout guide from among the guides owned by a view.

Identifiers starting with “NS” or “UI” are reserved by the system. The system may assign these identifiers to the guides it creates.

## See Also

- [var layoutFrame: CGRect](uilayoutguide/layoutframe.md)
  The layout guide’s frame in its owning view’s coordinate system.
- [var owningView: UIView?](uilayoutguide/owningview.md)
  The view that owns this layout guide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilayoutguide/identifier)*