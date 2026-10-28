# sharedSystemTypesetter

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns a shared instance of a reentrant typesetter.

**Availability**:
- macOS

## Declaration

```swift
class var sharedSystemTypesetter: NSTypesetter { get }
```

```objc
@property (class, strong, readonly) NSTypesetter * sharedSystemTypesetter;
```

## Return Value

The shared system typesetter. This typesetter is reentrant.

## See Also

### Related Documentation
- [class NSATSTypesetter](../nsatstypesetter.md)
  A concrete typesetter object that places glyphs during the text layout process.
### Getting a typesetter
- [class func sharedSystemTypesetter(for: NSLayoutManager.TypesetterBehavior) -> Any](./sharedsystemtypesetter%28for%29.md)
  Returns a shared instance of a reentrant typesetter that implements typesetting with the specified behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/sharedsystemtypesetter)*