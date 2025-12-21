# setName(_:)

**Framework**: AppKit  
**Kind**: method

Registers the image object under the specified name.

**Availability**:
- macOS ?+

## Declaration

```swift
func setName(_ string: NSImage.Name?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the receiver was successfully registered with the given name; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

If the receiver is already registered under a different name, this method unregisters the other name. If a different image is already registered under the name specified in `aString`, this method does nothing and returns [`false`](https://developer.apple.com/documentation/Swift/false).

When naming an image using this method, it is convention not to include filename extensions in the names you specify. That way, you can easily distinguish between images you have named explicitly and those you want to load from the app’s bundle. For information about the rules used to search for images, and for information about the ownership policy of named images, see the [`init(named:)`](nsimage/init(named:).md) method.

## Parameters

- `string`: The name to associate with the receiver. Specify   if you want to remove the image from the image cache.

## See Also

- [Configuring and displaying symbol images in your UI](../UIKit/configuring-and-displaying-symbol-images-in-your-ui.md)
  Create scalable images that integrate with your app’s text, and adjust the appearance of those images dynamically.
- [init?(named: NSImage.Name)](nsimage/init(named:).md)
  Returns the image object associated with the specified name.
- [convenience init?(systemSymbolName: String, accessibilityDescription: String?)](nsimage/init(systemsymbolname:accessibilitydescription:).md)
  Creates a symbol image with the system symbol name and accessibility description you specify.
- [convenience init?(systemSymbolName: String, variableValue: Double, accessibilityDescription: String?)](nsimage/init(systemsymbolname:variablevalue:accessibilitydescription:).md)
  Creates a symbol image with the system symbol name and variable value you specify.
- [convenience init?(symbolName: String, variableValue: Double)](nsimage/init(symbolname:variablevalue:).md)
  Creates a symbol image with the symbol name and variable value you specify.
- [convenience init?(symbolName: String, bundle: Bundle?, variableValue: Double)](nsimage/init(symbolname:bundle:variablevalue:).md)
- [convenience init(resource: ImageResource)](nsimage/init(resource:).md)
- [func name() -> NSImage.Name?](nsimage/name.md)
  Returns the name associated with the image, if any.
- [typealias Name](nsimage/name-swift.typealias.md)
  Named images, defined by the system or you, for use in your app.
- [convenience init(imageLiteralResourceName: String)](nsimage/init(imageliteralresourcename:).md)
  Creates an image initialized with the specified resource name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/setname(_:))*