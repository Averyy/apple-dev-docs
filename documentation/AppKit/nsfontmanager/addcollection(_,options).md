# addCollection(_:options:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds a specified font collection to the font manager with a given set of options.

**Availability**:
- macOS 10.0+ - Deprecated in 10.11

> **Deprecated**: Use [`show(_:withName:visibility:)`](../nsfontcollection/show%28_,withname,visibility%29.md) instead.

## Declaration

```swift
func addCollection(_ collectionName: String, options collectionOptions: NSFontCollectionOptions = []) -> Bool
```

```objc
- (BOOL) addCollection:(NSString *) collectionName options:(NSFontCollectionOptions) collectionOptions;
```

#### Return Value

[`true`](../../Swift/true.md) if the font collection was successfully added; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `collectionName`: The collection to add.
- `collectionOptions`: The option described in `Font Collection Mask`. This option is not yet implemented.

## See Also

### Deprecated methods
- [func availableFontNames(matching: NSFontDescriptor) -> [Any]?](./availablefontnames%28matching%29.md)
  Returns the names of the fonts that match the attributes in the given font descriptor.
- [func fontDescriptors(inCollection: String) -> [Any]?](./fontdescriptors%28incollection%29.md)
  Returns an array of the font descriptors in the specified collection.
- [func removeCollection(String) -> Bool](./removecollection%28_%29.md)
  Removes the specified font collection.
- [func addFontDescriptors([Any], toCollection: String)](./addfontdescriptors%28_,tocollection%29.md)
  Adds an array of font descriptors to the specified font collection.
- [func removeFontDescriptor(NSFontDescriptor, fromCollection: String)](./removefontdescriptor%28_,fromcollection%29.md)
  Removes the specified font descriptor from the specified collection.
- [func fontManager(Any, willIncludeFont: String) -> Bool](../../ObjectiveC/nsobject-swift.class/fontmanager%28_,willincludefont%29.md)
  Requests permission from the Font panel delegate to display the given font name in the Font panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/addcollection(_:options:))*