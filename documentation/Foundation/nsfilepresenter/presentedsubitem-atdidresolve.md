# presentedSubitem(at:didResolve:)

**Framework**: Foundation  
**Kind**: method

Tells the delegate that the item inside the presented directory had a version conflict resolved by an outside entity.

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
optional func presentedSubitem(at url: URL, didResolve version: NSFileVersion)
```

#### Discussion

Your delegate can use this method to respond to the resolution of a version conflict by a different file presenter. This might occur if a version of your application running on another device resolves the conflict first. You might then use this method to update your user interface to indicate that there is no longer a conflict.

## Parameters

- `url`: The URL of the item inside the presented directory that was in conflict. The item need not be at the top level of the presented directory but may itself be inside a nested subdirectory.
- `version`: The version object containing the conflicting change.

## See Also

- [func presentedItemDidGain(NSFileVersion)](nsfilepresenter/presenteditemdidgain(_:).md)
  Tells the delegate that a new version of the file or file package was added.
- [func presentedItemDidLose(NSFileVersion)](nsfilepresenter/presenteditemdidlose(_:).md)
  Tells the delegate that a version of the file or file package was removed.
- [func presentedItemDidResolveConflict(NSFileVersion)](nsfilepresenter/presenteditemdidresolveconflict(_:).md)
  Tells the delegate that some other entity resolved a version conflict for the presenter’s file or file package.
- [func presentedSubitem(at: URL, didGain: NSFileVersion)](nsfilepresenter/presentedsubitem(at:didgain:).md)
  Tells the delegate that the item inside the presented directory gained a new version.
- [func presentedSubitem(at: URL, didLose: NSFileVersion)](nsfilepresenter/presentedsubitem(at:didlose:).md)
  Tells the delegate that the item inside the presented directory lost an existing version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilepresenter/presentedsubitem(at:didresolve:))*