# sharedSystemTypesetter

**Framework**: AppKit  
**Kind**: property

Returns a shared instance of a reentrant typesetter.

**Availability**:
- macOS ?+

## Declaration

```swift
class var sharedSystemTypesetter: NSTypesetter { get }
```

#### Return Value

The shared system typesetter. This typesetter is reentrant.

## See Also

- [Text Layout Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextLayout/TextLayout.html#//apple_ref/doc/uid/10000158i)
- [class func sharedSystemTypesetter(for: NSLayoutManager.TypesetterBehavior) -> Any](nstypesetter/sharedsystemtypesetter(for:).md)
  Returns a shared instance of a reentrant typesetter that implements typesetting with the specified behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/sharedsystemtypesetter)*