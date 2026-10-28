# urlReadingFileURLsOnly

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Option for reading URLs to restrict the results to file URLs only.

**Availability**:
- macOS 10.6+

## Declaration

```swift
static let urlReadingFileURLsOnly: NSPasteboard.ReadingOptionKey
```

```c
extern NSPasteboardReadingOptionKey const NSPasteboardURLReadingFileURLsOnlyKey;
```

## Discussion

The value for this key is an `NSNumber` object with a boolean value.

## See Also

### Type Properties
- [static let urlReadingContentsConformToTypes: NSPasteboard.ReadingOptionKey](./urlreadingcontentsconformtotypes.md)
  Option for reading URLs to restrict the results to URLs with contents that conform to any of the provided UTI types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/readingoptionkey/urlreadingfileurlsonly)*