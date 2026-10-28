# setName(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Registers the image object under the specified name.

**Availability**:
- macOS

## Declaration

```swift
func setName(_ string: NSImage.Name?) -> Bool
```

```objc
- (BOOL) setName:(NSImageName) string;
```

## Return Value

[`true`](../../Swift/true.md) if the receiver was successfully registered with the given name; otherwise, [`false`](../../Swift/false.md).

## Discussion

If the receiver is already registered under a different name, this method unregisters the other name. If a different image is already registered under the name specified in `aString`, this method does nothing and returns [`false`](../../Swift/false.md).

When naming an image using this method, it is convention not to include filename extensions in the names you specify. That way, you can easily distinguish between images you have named explicitly and those you want to load from the app’s bundle. For information about the rules used to search for images, and for information about the ownership policy of named images, see the [`init(named:)`](./init%28named%29.md) method.

## Parameters

- `string`: The name to associate with the receiver. Specify `nil` if you want to remove the image from the image cache.

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
- [func name() -> NSImage.Name?](./name%28%29.md)
  Returns the name associated with the image, if any.
- [typealias Name](./name-swift.typealias.md)
  Named images, defined by the system or you, for use in your app.
- [convenience init(imageLiteralResourceName: String)](./init%28imageliteralresourcename%29.md)
  Creates an image initialized with the specified resource name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/setname(_:))*