# removeQuery(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Edits the query and exclusion arrays by removing the specified font descriptors.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func removeQuery(for descriptors: [NSFontDescriptor])
```

```objc
- (void) removeQueryForDescriptors:(NSArray<NSFontDescriptor *> *) descriptors;
```

## Parameters

- `descriptors`: The font descriptors to add to the query.

## See Also

### Getting the Font Descriptors
- [var queryDescriptors: [NSFontDescriptor]?](./querydescriptors.md)
  The font descriptors to include in query results.
- [func addQuery(for: [NSFontDescriptor])](./addquery%28for%29.md)
  Edits the query and exclusion arrays by adding the specified font descriptors.
- [var exclusionDescriptors: [NSFontDescriptor]?](./exclusiondescriptors.md)
  The font descriptors to exclude from query results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmutablefontcollection/removequery(for:))*