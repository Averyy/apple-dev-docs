# init(contentsOf:)

**Framework**: AppKit  
**Kind**: init

Initializes and returns an image object with the contents of the specified URL.

**Availability**:
- macOS ?+

## Declaration

```swift
convenience init?(contentsOf url: URL)
```

#### Return Value

An initialized `NSImage` object or `nil` if the method cannot create an image representation from the contents of the specified URL.

## Parameters

- `url`: The URL identifying the image.

## See Also

- [convenience init?(byReferencingFile: String)](nsimage/init(byreferencingfile:).md)
  Initializes and returns an image object using the specified file.
- [convenience init(byReferencing: URL)](nsimage/init(byreferencing:).md)
  Initializes and returns an image object using the specified URL.
- [convenience init?(contentsOfFile: String)](nsimage/init(contentsoffile:).md)
  Initializes and returns an image object with the contents of the specified file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/init(contentsof:))*