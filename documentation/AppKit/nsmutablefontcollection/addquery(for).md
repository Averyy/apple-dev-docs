# addQuery(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Edits the query and exclusion arrays by adding the specified font descriptors.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func addQuery(for descriptors: [NSFontDescriptor])
```

```objc
- (void) addQueryForDescriptors:(NSArray<NSFontDescriptor *> *) descriptors;
```

## Parameters

- `descriptors`: The font descriptors to add to the query.

## See Also

### Getting the Font Descriptors
- [var queryDescriptors: [NSFontDescriptor]?](./querydescriptors.md)
  The font descriptors to include in query results.
- [func removeQuery(for: [NSFontDescriptor])](./removequery%28for%29.md)
  Edits the query and exclusion arrays by removing the specified font descriptors.
- [var exclusionDescriptors: [NSFontDescriptor]?](./exclusiondescriptors.md)
  The font descriptors to exclude from query results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmutablefontcollection/addquery(for:))*