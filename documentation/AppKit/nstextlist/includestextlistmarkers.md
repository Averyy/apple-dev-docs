# includesTextListMarkers

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A Boolean value that indicates whether TextKit includes text list markers in the contents.

**Availability**:
- macOS 26.0+

## Declaration

```swift
class var includesTextListMarkers: Bool { get }
```

```objc
@property (class, readonly) BOOL includesTextListMarkers;
```

## Discussion

The default value is `false`.

## See Also

### Getting list options
- [var isOrdered: Bool](./isordered.md)
- [var listOptions: NSTextList.Options](./listoptions.md)
  Returns the list options mask value of the receiver.
- [NSTextList.Options](./options.md)
  Values that available options for text list items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlist/includestextlistmarkers)*