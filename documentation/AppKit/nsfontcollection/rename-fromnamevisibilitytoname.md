# rename(fromName:visibility:toName:)

**Framework**: Appkit  
**Kind**: method

Renames the font collection with the specified name and visibility to the second name specified.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class func rename(fromName oldName: NSFontCollection.Name, visibility: NSFontCollection.Visibility, toName newName: NSFontCollection.Name) throws
```

#### Discussion

Named collections are shown by user interfaces such as the Font panel. When you change the collection, you must show it again to see the changes reflected on disk or in the Font panel.

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `oldName`: The collection to rename.
- `visibility`: The visibility of the collection to rename.
- `newName`: The new name to give to the collection.

## See Also

- [class func show(NSFontCollection, withName: NSFontCollection.Name, visibility: NSFontCollection.Visibility) throws](nsfontcollection/show(_:withname:visibility:).md)
  Make the given font collection visible by giving it a name.
- [class func hide(withName: NSFontCollection.Name, visibility: NSFontCollection.Visibility) throws](nsfontcollection/hide(withname:visibility:).md)
  Remove from view the named font collection with the specified visibility.
- [class var allFontCollectionNames: [NSFontCollection.Name]](nsfontcollection/allfontcollectionnames.md)
  Returns all named collections visible to this process.
- [NSFontCollection.Name](nsfontcollection/name.md)
  The constants represent the standard mutable collection names—these names are included in the list of [`allFontCollectionNames`](nsfontcollection/allfontcollectionnames.md)–they have special meaning to the Cocoa font system and should not be hidden or renamed.
- [NSFontCollection.Visibility](nsfontcollection/visibility.md)
  Constants that specify the visibility of font collections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollection/rename(fromname:visibility:toname:))*