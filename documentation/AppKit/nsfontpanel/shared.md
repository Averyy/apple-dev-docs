# shared

**Framework**: AppKit  
**Kind**: property

Returns the single `NSFontPanel` instance for the application, creating it if necessary.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class var shared: NSFontPanel { get }
```

#### Return Value

The `NSFontPanel` instance for the application.

## See Also

- [Cocoa Text Architecture Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/TextFonts/Conceptual/CocoaTextArchitecture/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009459)
- [class func setFontPanelFactory(AnyClass?)](nsfontmanager/setfontpanelfactory(_:).md)
  Sets the class that creates the shared Font panel object.
- [class var sharedFontPanelExists: Bool](nsfontpanel/sharedfontpanelexists.md)
  Returns [`true`](https://developer.apple.com/documentation/swift/true) if the shared Font panel has been created, [`false`](https://developer.apple.com/documentation/swift/false) if it hasn’t.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontpanel/shared)*