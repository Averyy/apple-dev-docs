# presentedSubitem(at:didGain:)

**Framework**: Foundation  
**Kind**: method

Tells the delegate that the item inside the presented directory gained a new version.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func presentedSubitem(at url: URL, didGain version: NSFileVersion)
```

#### Discussion

Your delegate can use this method to determine how to incorporate data from the new version of the item. This might involve incorporating the version silently or asking the user about how to proceed.

## Parameters

- `url`: The URL of the item inside the presented directory that gained a new version. The item need not be at the top level of the presented directory but may itself be inside a nested subdirectory.
- `version`: The file version object containing information about the new file version.

## See Also

- [func presentedItemDidGain(NSFileVersion)](nsfilepresenter/presenteditemdidgain(_:).md)
  Tells the delegate that a new version of the file or file package was added.
- [func presentedItemDidLose(NSFileVersion)](nsfilepresenter/presenteditemdidlose(_:).md)
  Tells the delegate that a version of the file or file package was removed.
- [func presentedItemDidResolveConflict(NSFileVersion)](nsfilepresenter/presenteditemdidresolveconflict(_:).md)
  Tells the delegate that some other entity resolved a version conflict for the presenter’s file or file package.
- [func presentedSubitem(at: URL, didLose: NSFileVersion)](nsfilepresenter/presentedsubitem(at:didlose:).md)
  Tells the delegate that the item inside the presented directory lost an existing version.
- [func presentedSubitem(at: URL, didResolve: NSFileVersion)](nsfilepresenter/presentedsubitem(at:didresolve:).md)
  Tells the delegate that the item inside the presented directory had a version conflict resolved by an outside entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilepresenter/presentedsubitem(at:didgain:))*