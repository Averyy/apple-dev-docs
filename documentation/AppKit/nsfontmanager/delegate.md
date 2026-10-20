# delegate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The font manager’s delegate.

**Availability**:
- macOS 10.0+ - Deprecated in 10.11

> **Deprecated**: There is no font manager delegate; don’t use this property.

## Declaration

```swift
unowned(unsafe) var delegate: AnyObject? { get set }
```

```objc
@property (assign, nullable) id delegate;
```

## See Also

### Deprecated properties
- [static var applicationOnlyMask: NSFontCollectionOptions](../nsfontcollectionoptions/applicationonlymask.md)
  Makes the collection available only to the application.
- [var collectionNames: [Any]](./collectionnames.md)
  The names of the currently loaded font collections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/delegate)*