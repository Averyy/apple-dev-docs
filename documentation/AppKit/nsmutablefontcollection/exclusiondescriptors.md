# exclusionDescriptors

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The font descriptors to exclude from query results.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var exclusionDescriptors: [NSFontDescriptor]? { get set }
```

```objc
@property (copy, nullable) NSArray<NSFontDescriptor *> * exclusionDescriptors;
```

## See Also

### Getting the Font Descriptors
- [var queryDescriptors: [NSFontDescriptor]?](./querydescriptors.md)
  The font descriptors to include in query results.
- [func addQuery(for: [NSFontDescriptor])](./addquery%28for%29.md)
  Edits the query and exclusion arrays by adding the specified font descriptors.
- [func removeQuery(for: [NSFontDescriptor])](./removequery%28for%29.md)
  Edits the query and exclusion arrays by removing the specified font descriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmutablefontcollection/exclusiondescriptors)*