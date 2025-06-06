# init(contentsOfFile:)

**Framework**: AppKit  
**Kind**: init

Initializes and returns an image object with the contents of the specified file.

**Availability**:
- macOS ?+

## Declaration

```swift
convenience init?(contentsOfFile fileName: String)
```

#### Return Value

An initialized `NSImage` object or `nil` if the method cannot create an image representation from the contents of the specified file.

#### Discussion

Unlike [`init(byReferencingFile:)`](nsimage/init(byreferencingfile:).md), which initializes an `NSImage` object lazily, this method immediately opens the specified file and creates one or more image representations from its data.

The `filename` parameter should include the file extension that identifies the type of the image data. This method looks for an `NSImageRep` subclass that handles that data type from among those registered with `NSImage`.

## Parameters

- `fileName`: A full or relative path name specifying the file with the desired image data. Relative paths must be relative to the current working directory.

## See Also

- [convenience init?(byReferencingFile: String)](nsimage/init(byreferencingfile:).md)
  Initializes and returns an image object using the specified file.
- [convenience init(byReferencing: URL)](nsimage/init(byreferencing:).md)
  Initializes and returns an image object using the specified URL.
- [convenience init?(contentsOf: URL)](nsimage/init(contentsof:).md)
  Initializes and returns an image object with the contents of the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/init(contentsoffile:))*