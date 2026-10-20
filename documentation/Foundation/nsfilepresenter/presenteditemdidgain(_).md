# presentedItemDidGain(_:)

**Framework**: Foundation  
**Kind**: method

Tells the delegate that a new version of the file or file package was added.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func presentedItemDidGain(_ version: NSFileVersion)
```

#### Discussion

Your delegate can use this method to determine how to incorporate data from the new version of the file or file package. If the file has not been modified by your code, you might simply update to the new version quietly. However, if your application has its own changes, you might need to ask the user how to proceed.

## Parameters

- `version`: The file version object containing information about the new file version.

## See Also

- [func presentedItemDidLose(NSFileVersion)](nsfilepresenter/presenteditemdidlose(_:).md)
  Tells the delegate that a version of the file or file package was removed.
- [func presentedItemDidResolveConflict(NSFileVersion)](nsfilepresenter/presenteditemdidresolveconflict(_:).md)
  Tells the delegate that some other entity resolved a version conflict for the presenter’s file or file package.
- [func presentedSubitem(at: URL, didGain: NSFileVersion)](nsfilepresenter/presentedsubitem(at:didgain:).md)
  Tells the delegate that the item inside the presented directory gained a new version.
- [func presentedSubitem(at: URL, didLose: NSFileVersion)](nsfilepresenter/presentedsubitem(at:didlose:).md)
  Tells the delegate that the item inside the presented directory lost an existing version.
- [func presentedSubitem(at: URL, didResolve: NSFileVersion)](nsfilepresenter/presentedsubitem(at:didresolve:).md)
  Tells the delegate that the item inside the presented directory had a version conflict resolved by an outside entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilepresenter/presenteditemdidgain(_:))*