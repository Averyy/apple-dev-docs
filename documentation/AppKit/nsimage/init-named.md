# init(named:)

**Framework**: AppKit  
**Kind**: init

Returns the image object associated with the specified name.

**Availability**:
- macOS ?+

## Declaration

```swift
init?(named name: NSImage.Name)
```

#### Return Value

The `NSImage` object associated with the specified name or `nil` if no such image was found.

#### Discussion

This method searches for named images in several places, returning the first image it finds matching the given name. The order of the search is as follows:

1. Search for an object whose name was set explicitly using the [`setName(_:)`](nsimage/setname(_:).md) method and currently resides in the image cache.
2. Search the app’s main bundle for a file whose name matches the specified string. (For information on how the bundle is searched, see “[`Accessing a Bundle’s Contents`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/AccessingaBundlesContents/AccessingaBundlesContents.html#//apple_ref/doc/uid/10000123i-CH104)” in [`Bundle Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/Introduction/Introduction.html#//apple_ref/doc/uid/10000123i).)
3. Search the Application Kit framework for a shared image with the specified name.

When looking for files in the app bundle, it is better (but not required) to include the filename extension in the `name` parameter. When naming an image with the [`setName(_:)`](nsimage/setname(_:).md) method, it is convention not to include filename extensions in the names you specify. That way, you can easily distinguish between images you have named explicitly and those you want to load from the app’s bundle.

One particularly useful image you can retrieve is your app’s icon. This image is set by Cocoa automatically and accessible using the [`applicationIconName`](nsimage/applicationiconname.md) constant. Icons for other apps can be obtained through the use of methods declared in the [`NSWorkspace`](nsworkspace.md) class. You can also retrieve many of the standard system images using Cocoa defined constants; for more information, see the `Image Template Constants`, `Sharing Permissions Named Images`, `System Entity Images`, `Toolbar Named Images`, and `View Type Template Images` sections for applicable constants.

If an app is linked on macOS 10.5 or later, images requested using this method and whose name ends in the word “Template” are automatically marked as template images.

The `NSImage` class may cache a reference to the returned image object for performance in some cases. However, the class holds onto cached objects only while the object exists. If all strong references to the image are subsequently removed, the object may be quietly removed from the cache. Thus, if you plan to hold onto a returned image object, you must maintain a strong reference to it like you would any Cocoa object. You can clear an image object from the cache explicitly by calling the object’s [`setName(_:)`](nsimage/setname(_:).md) method and specifying `nil` for the image name.

## Parameters

- `name`: The name associated with the desired image. This can be a name you assigned to the image or the name of an image file in your app bundle.

## See Also

- [class func imageFileTypes() -> [String]](nsimage/imagefiletypes.md)
  Returns an array of strings identifying the image types supported by the registered image representation objects.
- [func icon(forFile: String) -> NSImage](nsworkspace/icon(forfile:).md)
  Returns an image containing the icon for the specified file.
- [Configuring and displaying symbol images in your UI](../UIKit/configuring-and-displaying-symbol-images-in-your-ui.md)
  Create scalable images that integrate with your app’s text, and adjust the appearance of those images dynamically.
- [convenience init?(systemSymbolName: String, accessibilityDescription: String?)](nsimage/init(systemsymbolname:accessibilitydescription:).md)
  Creates a symbol image with the system symbol name and accessibility description you specify.
- [convenience init?(systemSymbolName: String, variableValue: Double, accessibilityDescription: String?)](nsimage/init(systemsymbolname:variablevalue:accessibilitydescription:).md)
  Creates a symbol image with the system symbol name and variable value you specify.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/init(named:))*