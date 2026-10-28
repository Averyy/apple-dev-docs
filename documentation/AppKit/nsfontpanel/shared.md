# shared

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns the single `NSFontPanel` instance for the application, creating it if necessary.

**Availability**:
- macOS

## Declaration

```swift
class var shared: NSFontPanel { get }
```

```objc
@property (class, strong, readonly) NSFontPanel * sharedFontPanel;
```

## Return Value

The `NSFontPanel` instance for the application.

## See Also

### Related Documentation
- [class func setFontPanelFactory(AnyClass?)](../nsfontmanager/setfontpanelfactory%28_%29.md)
  Sets the class that creates the shared Font panel object.
### Getting the Font Panel
- [class var sharedFontPanelExists: Bool](./sharedfontpanelexists.md)
  A Boolean value that indicates whether the shared Font panel has been created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontpanel/shared)*