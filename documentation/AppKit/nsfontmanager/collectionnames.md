# collectionNames

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The names of the currently loaded font collections.

**Availability**:
- macOS 10.0+ - Deprecated in 10.11

> **Deprecated**: Use [`allFontCollectionNames`](../nsfontcollection/allfontcollectionnames.md) instead.

## Declaration

```swift
var collectionNames: [Any] { get }
```

```objc
@property (copy, readonly) NSArray * collectionNames;
```

## See Also

### Related Documentation
- [func fontDescriptors(inCollection: String) -> [Any]?](./fontdescriptors%28incollection%29.md)
  Returns an array of the font descriptors in the specified collection.
### Deprecated properties
- [static var applicationOnlyMask: NSFontCollectionOptions](../nsfontcollectionoptions/applicationonlymask.md)
  Makes the collection available only to the application.
- [var delegate: AnyObject?](./delegate.md)
  The font manager’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/collectionnames)*