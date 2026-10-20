# queryDescriptors

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The font descriptors to include in query results.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var queryDescriptors: [NSFontDescriptor]? { get set }
```

```objc
@property (copy, nullable) NSArray<NSFontDescriptor *> * queryDescriptors;
```

## See Also

### Getting the Font Descriptors
- [func addQuery(for: [NSFontDescriptor])](./addquery%28for%29.md)
  Edits the query and exclusion arrays by adding the specified font descriptors.
- [func removeQuery(for: [NSFontDescriptor])](./removequery%28for%29.md)
  Edits the query and exclusion arrays by removing the specified font descriptors.
- [var exclusionDescriptors: [NSFontDescriptor]?](./exclusiondescriptors.md)
  The font descriptors to exclude from query results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmutablefontcollection/querydescriptors)*