# init(systemSymbolName:variableValue:accessibilityDescription:)

**Framework**: AppKit  
**Kind**: init

Creates a symbol image with the system symbol name and variable value you specify.

**Availability**:
- macOS 13.0+

## Declaration

```swift
convenience init?(systemSymbolName name: String, variableValue value: Double, accessibilityDescription description: String?)
```

#### Discussion

The `value` parameter is valid for symbols that support variable rendering.

To look up the names of system symbol images, download the SF Symbols app from [`Apple Design Resources`](https://developer.apple.comhttps://developer.apple.com/design/resources/).

## Parameters

- `name`: The name of the system symbol image.
- `value`: The value the system uses to customize the symbol’s content, between   and  .
- `description`: The accessibility description for the symbol image, if any.

## See Also

- [Configuring and displaying symbol images in your UI](../UIKit/configuring-and-displaying-symbol-images-in-your-ui.md)
  Create scalable images that integrate with your app’s text, and adjust the appearance of those images dynamically.
- [init?(named: NSImage.Name)](nsimage/init(named:).md)
  Returns the image object associated with the specified name.
- [convenience init?(systemSymbolName: String, accessibilityDescription: String?)](nsimage/init(systemsymbolname:accessibilitydescription:).md)
  Creates a symbol image with the system symbol name and accessibility description you specify.
- [convenience init?(symbolName: String, variableValue: Double)](nsimage/init(symbolname:variablevalue:).md)
  Creates a symbol image with the symbol name and variable value you specify.
- [convenience init?(symbolName: String, bundle: Bundle?, variableValue: Double)](nsimage/init(symbolname:bundle:variablevalue:).md)
- [convenience init(resource: ImageResource)](nsimage/init(resource:).md)
- [func setName(NSImage.Name?) -> Bool](nsimage/setname(_:).md)
  Registers the image object under the specified name.
- [func name() -> NSImage.Name?](nsimage/name.md)
  Returns the name associated with the image, if any.
- [typealias Name](nsimage/name-swift.typealias.md)
  Named images, defined by the system or you, for use in your app.
- [convenience init(imageLiteralResourceName: String)](nsimage/init(imageliteralresourcename:).md)
  Creates an image initialized with the specified resource name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/init(systemsymbolname:variablevalue:accessibilitydescription:))*