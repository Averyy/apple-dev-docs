# pathForImageResource(_:)

**Framework**: Foundation  
**Kind**: method

Returns the location of the specified image resource file.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func pathForImageResource(_ name: NSImage.Name) -> String?
```

#### Return Value

The absolute pathname of the resource file or `nil` if the file is not found.

#### Discussion

Image resources are those files in the bundle that are recognized by the `NSImage` class, including those that can be converted using the Image IO framework.

## Parameters

- `name`: The name of the image resource file, without any pathname information. Including a filename extension is optional.

## See Also

- [func path(forResource: String?, ofType: String?) -> String?](bundle/path(forresource:oftype:).md)
  Returns the full pathname for the resource identified by the specified name and file extension.
- [func urlForImageResource(NSImage.Name) -> URL?](bundle/urlforimageresource(_:).md)
  Returns the location of the specified image resource as an NSURL.
- [func image(forResource: NSImage.Name) -> NSImage?](bundle/image(forresource:).md)
  Returns an `NSImage` instance associated with the specified name, which can be backed by multiple files representing different resolution versions of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/pathforimageresource(_:))*