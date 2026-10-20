# defaultFileName

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The initial value for the user-editable filename shown in the name field of the PDF panel.

**Availability**:
- macOS 10.9+

## Declaration

```swift
var defaultFileName: String { get set }
```

```objc
@property (copy) NSString * defaultFileName;
```

#### Discussion

The `defaultFileName` string should never include a file extension. By default, the string’s value is “Untitled” (or its equivalent for the current locale).

## See Also

### Managing the Contents of a PDF Panel
- [var accessoryController: NSViewController?](./accessorycontroller.md)
  A view controller for the accessory view that the panel can present.
- [var options: NSPDFPanel.Options](./options-swift.property.md)
  A set of configuration options that determine the accessory views the PDF panel should display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspdfpanel/defaultfilename)*