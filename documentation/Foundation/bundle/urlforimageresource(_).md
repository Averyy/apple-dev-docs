# urlForImageResource(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the location of the specified image resource as an NSURL.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func urlForImageResource(_ name: NSImage.Name) -> URL?
```

```objc
- (NSURL *) URLForImageResource:(NSImageName) name;
```

## Return Value

An `NSURL` for the resource file or `nil` if the file was not found.

## Parameters

- `name`: The name of the image resource file. Including a filename extension is optional.

## See Also

### Finding image resources
- [func pathForImageResource(NSImage.Name) -> String?](./pathforimageresource%28_%29.md)
  Returns the location of the specified image resource file.
- [func image(forResource: NSImage.Name) -> NSImage?](./image%28forresource%29.md)
  Returns an `NSImage` instance associated with the specified name, which can be backed by multiple files representing different resolution versions of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/urlforimageresource(_:))*