# name()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the name associated with the image, if any.

**Availability**:
- macOS

## Declaration

```swift
func name() -> NSImage.Name?
```

```objc
- (NSImageName) name;
```

## Return Value

The name associated with the image, or `nil` if it has no associated name.

## See Also

### Creating Images by Name
- [Configuring and displaying symbol images in your UI](../../UIKit/configuring-and-displaying-symbol-images-in-your-ui.md)
  Create scalable images that integrate with your app’s text, and adjust the appearance of those images dynamically.
- [init?(named: NSImage.Name)](./init%28named%29.md)
  Returns the image object associated with the specified name.
- [convenience init?(systemSymbolName: String, accessibilityDescription: String?)](./init%28systemsymbolname,accessibilitydescription%29.md)
  Creates a symbol image with the system symbol name and accessibility description you specify.
- [convenience init?(systemSymbolName: String, variableValue: Double, accessibilityDescription: String?)](./init%28systemsymbolname,variablevalue,accessibilitydescription%29.md)
  Creates a symbol image with the system symbol name and variable value you specify.
- [convenience init?(symbolName: String, variableValue: Double)](./init%28symbolname,variablevalue%29.md)
  Creates a symbol image with the symbol name and variable value you specify.
- [convenience init?(symbolName: String, bundle: Bundle?, variableValue: Double)](./init%28symbolname,bundle,variablevalue%29.md)
  Creates a symbol image with the specified symbol name and variable value.
- [convenience init(resource: ImageResource)](./init%28resource%29.md)
  Initialize a `NSImage` with an image resource.
- [func setName(NSImage.Name?) -> Bool](./setname%28_%29.md)
  Registers the image object under the specified name.
- [typealias Name](./name-swift.typealias.md)
  Named images, defined by the system or you, for use in your app.
- [convenience init(imageLiteralResourceName: String)](./init%28imageliteralresourcename%29.md)
  Creates an image initialized with the specified resource name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/name())*