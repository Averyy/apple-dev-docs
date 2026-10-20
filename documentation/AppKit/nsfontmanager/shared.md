# shared

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns the shared instance of the font manager for the application, creating it if necessary.

**Availability**:
- macOS

## Declaration

```swift
class var shared: NSFontManager { get }
```

```objc
@property (class, strong, readonly) NSFontManager * sharedFontManager;
```

#### Return Value

The shared font manager.

## See Also

### Related Documentation
- [class func setFontManagerFactory(AnyClass?)](./setfontmanagerfactory%28_%29.md)
  Sets the class that creates the shared font manager object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/shared)*