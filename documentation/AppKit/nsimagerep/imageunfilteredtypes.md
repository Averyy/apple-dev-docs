# imageUnfilteredTypes

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns an array of UTI strings identifying the image types supported directly by the ime representation.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class var imageUnfilteredTypes: [String] { get }
```

```objc
@property (class, copy, readonly) NSArray<NSString *> * imageUnfilteredTypes;
```

## Return Value

An array of `NSString` objects, each of which contains a UTI identifying a supported image type. Some sample image-related UTI strings include “`public.image`”, “`public.jpeg`”, and “`public.tiff`”. For a list of supported types, see `UTCoreTypes.h`.

## Discussion

The returned list includes UTI strings only for those file types that are supported directly by the receiver. It does not include types that are supported through user-installed filter services. You can use the returned UTI strings with any method that supports UTIs.

## See Also

### Determining Types for Images
- [class func canInit(with: Data) -> Bool](./caninit%28with%29-6zv56.md)
  Returns a Boolean value that indicates whether the image representation can initialize itself from the specified data.
- [class func canInit(with: NSPasteboard) -> Bool](./caninit%28with%29-56pum.md)
  Returns a Boolean value that indicates whether the receiver can initialize itself from the data on the specified pasteboard.
- [class var imageTypes: [String]](./imagetypes.md)
  Returns an array of UTI strings identifying the image types supported by the image representation, either directly or through a user-installed filter service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/imageunfilteredtypes)*