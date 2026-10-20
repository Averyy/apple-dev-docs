# addFontDescriptors(_:toCollection:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds an array of font descriptors to the specified font collection.

**Availability**:
- macOS 10.0+ - Deprecated in 10.11

> **Deprecated**: Use [`addQuery(for:)`](../nsmutablefontcollection/addquery%28for%29.md) instead.

## Declaration

```swift
func addFontDescriptors(_ descriptors: [Any], toCollection collectionName: String)
```

```objc
- (void) addFontDescriptors:(NSArray *) descriptors toCollection:(NSString *) collectionName;
```

## Parameters

- `descriptors`: The font descriptors to add.
- `collectionName`: The font collection to which descriptors are added.

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
- [func removeFontDescriptor(NSFontDescriptor, fromCollection: String)](./removefontdescriptor%28_,fromcollection%29.md)
  Removes the specified font descriptor from the specified collection.
- [func fontManager(Any, willIncludeFont: String) -> Bool](../../ObjectiveC/nsobject-swift.class/fontmanager%28_,willincludefont%29.md)
  Requests permission from the Font panel delegate to display the given font name in the Font panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/addfontdescriptors(_:tocollection:))*