# hide(withName:visibility:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Remove from view the named font collection with the specified visibility.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class func hide(withName name: NSFontCollection.Name, visibility: NSFontCollection.Visibility) throws
```

```objc
+ (BOOL) hideFontCollectionWithName:(NSFontCollectionName) name visibility:(NSFontCollectionVisibility) visibility error:(NSError **) error;
```

#### Discussion

For a persistent font collection, this method deletes the named font collection from disk.

> **Handling Errors in Swift**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `name`: The name of the collection.
- `visibility`: The visibility of the collection.

## See Also

### Naming the Font Collection
- [class func rename(fromName: NSFontCollection.Name, visibility: NSFontCollection.Visibility, toName: NSFontCollection.Name) throws](./rename%28fromname,visibility,toname%29.md)
  Renames the font collection with the specified name and visibility to the second name specified.
- [class func show(NSFontCollection, withName: NSFontCollection.Name, visibility: NSFontCollection.Visibility) throws](./show%28_,withname,visibility%29.md)
  Make the given font collection visible by giving it a name.
- [class var allFontCollectionNames: [NSFontCollection.Name]](./allfontcollectionnames.md)
  Returns all named collections visible to this process.
- [NSFontCollection.Name](./name.md)
  The constants represent the standard mutable collection names—these names are included in the list of [`allFontCollectionNames`](./allfontcollectionnames.md)–they have special meaning to the Cocoa font system and should not be hidden or renamed.
- [NSFontCollection.Visibility](./visibility.md)
  Constants that specify the visibility of font collections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollection/hide(withname:visibility:))*