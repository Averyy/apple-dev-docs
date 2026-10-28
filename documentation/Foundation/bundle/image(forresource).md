# image(forResource:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns an `NSImage` instance associated with the specified name, which can be backed by multiple files representing different resolution versions of the image.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func image(forResource name: NSImage.Name) -> NSImage?
```

```objc
- (NSImage *) imageForResource:(NSImageName) name;
```

## Return Value

The `NSImage` object associated with the specified name, or `nil` if no file is found.

## Discussion

This method accommodates Apple’s naming conventions for high-resolution versions of the image. For example, if your bundle contains files named `button.png`, `button@2x.png`, and `button.pdf` then `imageForResource:@"button"` returns an `NSImage` object backed by all three files. Each time the `NSImage` object is drawn, it selects the representation best for the drawing context.

Images requested using this method whose name ends in the word `Template` are automatically marked as template images.

This method does not look up images based on [`setName(_:)`](../../AppKit/nsimage/setname%28_%29.md) or get named system images. Use [`init(named:)`](../../AppKit/nsimage/init%28named%29.md) for that purpose.

This method does not cache its search results.

## Parameters

- `name`: The filename of the image resource file. Including a filename extension is optional.

## See Also

### Related Documentation
- [init?(named: NSImage.Name)](../../AppKit/nsimage/init%28named%29.md)
  Returns the image object associated with the specified name.
### Finding image resources
- [func urlForImageResource(NSImage.Name) -> URL?](./urlforimageresource%28_%29.md)
  Returns the location of the specified image resource as an NSURL.
- [func pathForImageResource(NSImage.Name) -> String?](./pathforimageresource%28_%29.md)
  Returns the location of the specified image resource file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/image(forresource:))*