# prepareForNewContents(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Prepares the pasteboard to receive new contents, removing the existing pasteboard contents.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func prepareForNewContents(with options: NSPasteboard.ContentsOptions = []) -> Int
```

```objc
- (NSInteger) prepareForNewContentsWithOptions:(NSPasteboardContentsOptions) options;
```

## See Also

### Preparing the pasteboard for content
- [NSPasteboard.ContentsOptions](./contentsoptions.md)
  Options for preparing the pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/preparefornewcontents(with:))*