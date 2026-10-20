# identifier

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A string used to identify the layout guide.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var identifier: NSUserInterfaceItemIdentifier { get set }
```

```objc
@property (copy) NSUserInterfaceItemIdentifier identifier;
```

#### Discussion

By default, the `identifier` property is `nil`. You can assign a string to help identify this guide. This string appears as part of the guide’s description when the guide is printed to the console. You can also use the identifier to find a particular layout guide from among the guides owned by a view.

Identifiers starting with “NS” or “UI” are reserved by the system. The system may assign these identifiers to the guides it creates.

## See Also

### Working With Layout Guides
- [var frame: NSRect](./frame.md)
  The layout guide’s frame in its owning view’s coordinate system.
- [var owningView: NSView?](./owningview.md)
  The view that owns this layout guide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutguide/identifier)*