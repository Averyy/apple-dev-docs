# init(systemSymbolName:variableValue:accessibilityDescription:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a symbol image with the system symbol name and variable value you specify.

**Availability**:
- macOS 13.0+

## Declaration

```swift
convenience init?(systemSymbolName name: String, variableValue value: Double, accessibilityDescription description: String?)
```

```objc
+ (instancetype) imageWithSystemSymbolName:(NSString *) name variableValue:(double) value accessibilityDescription:(NSString *) description;
```

## Discussion

The `value` parameter is valid for symbols that support variable rendering.

To look up the names of system symbol images, download the SF Symbols app from [Apple Design Resources](https://developer.apple.com/design/resources/).

## Parameters

- `name`: The name of the system symbol image.
- `value`: The value the system uses to customize the symbol’s content, between `0` and `1`.
- `description`: The accessibility description for the symbol image, if any.

## See Also

### Creating Images by Name
- [Configuring and displaying symbol images in your UI](../../UIKit/configuring-and-displaying-symbol-images-in-your-ui.md)
  Create scalable images that integrate with your app’s text, and adjust the appearance of those images dynamically.
- [init?(named: NSImage.Name)](./init%28named%29.md)
  Returns the image object associated with the specified name.
- [convenience init?(systemSymbolName: String, accessibilityDescription: String?)](./init%28systemsymbolname,accessibilitydescription%29.md)
  Creates a symbol image with the system symbol name and accessibility description you specify.
- [convenience init?(symbolName: String, variableValue: Double)](./init%28symbolname,variablevalue%29.md)
  Creates a symbol image with the symbol name and variable value you specify.
- [convenience init?(symbolName: String, bundle: Bundle?, variableValue: Double)](./init%28symbolname,bundle,variablevalue%29.md)
  Creates a symbol image with the specified symbol name and variable value.
- [convenience init(resource: ImageResource)](./init%28resource%29.md)
  Initialize a `NSImage` with an image resource.
- [func setName(NSImage.Name?) -> Bool](./setname%28_%29.md)
  Registers the image object under the specified name.
- [func name() -> NSImage.Name?](./name%28%29.md)
  Returns the name associated with the image, if any.
- [typealias Name](./name-swift.typealias.md)
  Named images, defined by the system or you, for use in your app.
- [convenience init(imageLiteralResourceName: String)](./init%28imageliteralresourcename%29.md)
  Creates an image initialized with the specified resource name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/init(systemsymbolname:variablevalue:accessibilitydescription:))*