# removeCollection(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes the specified font collection.

**Availability**:
- macOS 10.0+ - Deprecated in 10.11

> **Deprecated**: Use [`hide(withName:visibility:)`](../nsfontcollection/hide%28withname,visibility%29.md) instead.

## Declaration

```swift
func removeCollection(_ collectionName: String) -> Bool
```

```objc
- (BOOL) removeCollection:(NSString *) collectionName;
```

## Return Value

[`true`](../../Swift/true.md) if the font collection was successfully removed; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `collectionName`: The collection to remove.

## See Also

### Deprecated methods
- [func availableFontNames(matching: NSFontDescriptor) -> [Any]?](./availablefontnames%28matching%29.md)
  Returns the names of the fonts that match the attributes in the given font descriptor.
- [func fontDescriptors(inCollection: String) -> [Any]?](./fontdescriptors%28incollection%29.md)
  Returns an array of the font descriptors in the specified collection.
- [func addCollection(String, options: NSFontCollectionOptions) -> Bool](./addcollection%28_,options%29.md)
  Adds a specified font collection to the font manager with a given set of options.
- [func addFontDescriptors([Any], toCollection: String)](./addfontdescriptors%28_,tocollection%29.md)
  Adds an array of font descriptors to the specified font collection.
- [func removeFontDescriptor(NSFontDescriptor, fromCollection: String)](./removefontdescriptor%28_,fromcollection%29.md)
  Removes the specified font descriptor from the specified collection.
- [func fontManager(Any, willIncludeFont: String) -> Bool](../../ObjectiveC/nsobject-swift.class/fontmanager%28_,willincludefont%29.md)
  Requests permission from the Font panel delegate to display the given font name in the Font panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/removecollection(_:))*