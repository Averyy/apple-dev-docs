# urlReadingContentsConformToTypes

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Option for reading URLs to restrict the results to URLs with contents that conform to any of the provided UTI types.

**Availability**:
- macOS 10.6+

## Declaration

```swift
static let urlReadingContentsConformToTypes: NSPasteboard.ReadingOptionKey
```

```c
extern NSPasteboardReadingOptionKey const NSPasteboardURLReadingContentsConformToTypesKey;
```

#### Discussion

If the content type of a URL cannot be determined, it will not be considered to match.  The value for this key is an array of UTI type strings.

## See Also

### Type Properties
- [static let urlReadingFileURLsOnly: NSPasteboard.ReadingOptionKey](./urlreadingfileurlsonly.md)
  Option for reading URLs to restrict the results to file URLs only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/readingoptionkey/urlreadingcontentsconformtotypes)*