# fontDescriptors(inCollection:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns an array of the font descriptors in the specified collection.

**Availability**:
- macOS 10.0+ - Deprecated in 10.11

> **Deprecated**: Use [`matchingDescriptors`](../nsfontcollection/matchingdescriptors.md) instead.

## Declaration

```swift
func fontDescriptors(inCollection collectionNames: String) -> [Any]?
```

```objc
- (NSArray *) fontDescriptorsInCollection:(NSString *) collectionNames;
```

## Return Value

The font descriptors.

## Parameters

- `collectionNames`: The font collection for which to return descriptors.

## See Also

### Related Documentation
- [var collectionNames: [Any]](./collectionnames.md)
  The names of the currently loaded font collections.
### Deprecated methods
- [func availableFontNames(matching: NSFontDescriptor) -> [Any]?](./availablefontnames%28matching%29.md)
  Returns the names of the fonts that match the attributes in the given font descriptor.
- [func addCollection(String, options: NSFontCollectionOptions) -> Bool](./addcollection%28_,options%29.md)
  Adds a specified font collection to the font manager with a given set of options.
- [func removeCollection(String) -> Bool](./removecollection%28_%29.md)
  Removes the specified font collection.
- [func addFontDescriptors([Any], toCollection: String)](./addfontdescriptors%28_,tocollection%29.md)
  Adds an array of font descriptors to the specified font collection.
- [func removeFontDescriptor(NSFontDescriptor, fromCollection: String)](./removefontdescriptor%28_,fromcollection%29.md)
  Removes the specified font descriptor from the specified collection.
- [func fontManager(Any, willIncludeFont: String) -> Bool](../../ObjectiveC/nsobject-swift.class/fontmanager%28_,willincludefont%29.md)
  Requests permission from the Font panel delegate to display the given font name in the Font panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/fontdescriptors(incollection:))*