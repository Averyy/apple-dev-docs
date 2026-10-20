# focusView

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The currently focused view object.

**Availability**:
- macOS

## Declaration

```swift
class var focusView: NSView? { get }
```

```objc
@property (class, strong, readonly, nullable) NSView * focusView;
```

#### Discussion

The value in this property is `nil` if there is no focused view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/focusview)*