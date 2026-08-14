# init(byReferencing:)

**Framework**: AppKit  
**Kind**: init

Initializes and returns an image object using the specified URL.

**Availability**:
- macOS ?+

## Declaration

```swift
convenience init(byReferencing url: URL)
```

#### Return Value

An initialized `NSImage` object.

#### Discussion

This method initializes the image object lazily. It does not attempt to retrieve the data from the specified URL or create any image representations from that data until an app attempts to draw the image or request information about it.

The `url` parameter should include a file extension that identifies the type of the image data. The mechanism that actually creates the image representation looks for an [`NSImageRep`](nsimagerep.md) subclass that handles that data type from among those registered with `NSImage`.

Because this method doesn’t actually create image representations for the image data, your app should do error checking before attempting to use the image; one way to do so is by accessing the [`isValid`](nsimage/isvalid.md) property to check whether the image can be drawn.

This method invokes [`setDataRetained:`](nsimage/setdataretained:.md) with an argument of [`true`](https://developer.apple.com/documentation/swift/true), thus enabling it to hold onto its URL. When archiving an image created with this method, only the image’s URL is written to the archive.

## Parameters

- `url`: The URL identifying the image.

## See Also

- [convenience init?(byReferencingFile: String)](nsimage/init(byreferencingfile:).md)
  Initializes and returns an image object using the specified file.
- [convenience init?(contentsOfFile: String)](nsimage/init(contentsoffile:).md)
  Initializes and returns an image object with the contents of the specified file.
- [convenience init?(contentsOf: URL)](nsimage/init(contentsof:).md)
  Initializes and returns an image object with the contents of the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/init(byreferencing:))*