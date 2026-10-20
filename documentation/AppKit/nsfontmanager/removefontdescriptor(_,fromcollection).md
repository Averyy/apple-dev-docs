# removeFontDescriptor(_:fromCollection:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes the specified font descriptor from the specified collection.

**Availability**:
- macOS 10.0+ - Deprecated in 10.11

> **Deprecated**: Use [`removeQuery(for:)`](../nsmutablefontcollection/removequery%28for%29.md) instead.

## Declaration

```swift
func removeFontDescriptor(_ descriptor: NSFontDescriptor, fromCollection collection: String)
```

```objc
- (void) removeFontDescriptor:(NSFontDescriptor *) descriptor fromCollection:(NSString *) collection;
```

## Parameters

- `descriptor`: The font descriptor to remove.
- `collection`: The font collection from which to remove the descriptor.

## See Also

### Deprecated methods
- [func availableFontNames(matching: NSFontDescriptor) -> [Any]?](./availablefontnames%28matching%29.md)
  Returns the names of the fonts that match the attributes in the given font descriptor.
- [func fontDescriptors(inCollection: String) -> [Any]?](./fontdescriptors%28incollection%29.md)
  Returns an array of the font descriptors in the specified collection.
- [func addCollection(String, options: NSFontCollectionOptions) -> Bool](./addcollection%28_,options%29.md)
  Adds a specified font collection to the font manager with a given set of options.
- [func removeCollection(String) -> Bool](./removecollection%28_%29.md)
  Removes the specified font collection.
- [func addFontDescriptors([Any], toCollection: String)](./addfontdescriptors%28_,tocollection%29.md)
  Adds an array of font descriptors to the specified font collection.
- [func fontManager(Any, willIncludeFont: String) -> Bool](../../ObjectiveC/nsobject-swift.class/fontmanager%28_,willincludefont%29.md)
  Requests permission from the Font panel delegate to display the given font name in the Font panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/removefontdescriptor(_:fromcollection:))*