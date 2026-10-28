# init(contentsOf:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns an image object with the contents of the specified URL.

**Availability**:
- macOS

## Declaration

```swift
convenience init?(contentsOf url: URL)
```

```objc
- (instancetype) initWithContentsOfURL:(NSURL *) url;
```

## Return Value

An initialized `NSImage` object or `nil` if the method cannot create an image representation from the contents of the specified URL.

## Parameters

- `url`: The URL identifying the image.

## See Also

### Creating Images from Resource Files
- [convenience init?(byReferencingFile: String)](./init%28byreferencingfile%29.md)
  Initializes and returns an image object using the specified file.
- [convenience init(byReferencing: URL)](./init%28byreferencing%29.md)
  Initializes and returns an image object using the specified URL.
- [convenience init?(contentsOfFile: String)](./init%28contentsoffile%29.md)
  Initializes and returns an image object with the contents of the specified file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/init(contentsof:))*