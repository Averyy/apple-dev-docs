# documentCursor

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The cursor object used when the pointer lies over the view.

**Availability**:
- macOS

## Declaration

```swift
var documentCursor: NSCursor? { get set }
```

```objc
@property (strong, nullable) NSCursor * documentCursor;
```

#### Discussion

The default value of this property is `nil`, unless you specify a value in the xib file associated with the clip view (or scroll view). Note that the clip view’s document view may specify a cursor for its enclosing scroll view by setting [`enclosingScrollView`](../nsview/enclosingscrollview.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsclipview/documentcursor)*