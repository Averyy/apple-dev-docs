# placeholderView

**Framework**: ExtensionKit  
**Kind**: property  
**Role**: Instance Property

The view to display when the view controller has no app extension content to display.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 13.0+

## Declaration

*iOS, iPadOS, Mac Catalyst*

```swift
var placeholderView: UIView { get set }
```

*macOS*

```swift
var placeholderView: NSView { get set }
```

## See Also

### Configuring the view controller
- [var configuration: EXHostViewController.Configuration?](./configuration-swift.property.md)
  The information the host view controller uses to fetch the appropriate scene from an app extension.
- [EXHostViewController.Configuration](./configuration-swift.struct.md)
  An object that holds configuration options for a host view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/exhostviewcontroller/placeholderview)*