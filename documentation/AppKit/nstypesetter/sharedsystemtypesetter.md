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

- [class NSATSTypesetter](nsatstypesetter.md)
  A concrete typesetter object that places glyphs during the text layout process.
- [class func sharedSystemTypesetter(for: NSLayoutManager.TypesetterBehavior) -> Any](nstypesetter/sharedsystemtypesetter(for:).md)
  Returns a shared instance of a reentrant typesetter that implements typesetting with the specified behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/sharedsystemtypesetter)*