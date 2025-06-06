# relinquishPresentedItem(toWriter:)

**Framework**: AppKit  
**Kind**: method

**Availability**:
- macOS 10.7+

## Declaration

```swift
nonisolated
func relinquishPresentedItem(toWriter writer: @escaping ((() -> Void)?) -> Void)
```

## See Also

- [func accommodatePresentedItemDeletion(completionHandler: ((any Error)?) -> Void)](nsdocument/accommodatepresenteditemdeletion(completionhandler:).md)
- [func presentedItemDidChange()](nsdocument/presenteditemdidchange.md)
- [func presentedItemDidChangeUbiquityAttributes(Set<URLResourceKey>)](nsdocument/presenteditemdidchangeubiquityattributes(_:).md)
- [func presentedItemDidGain(NSFileVersion)](nsdocument/presenteditemdidgain(_:).md)
- [func presentedItemDidLose(NSFileVersion)](nsdocument/presenteditemdidlose(_:).md)
- [func presentedItemDidMove(to: URL)](nsdocument/presenteditemdidmove(to:).md)
- [func presentedItemDidResolveConflict(NSFileVersion)](nsdocument/presenteditemdidresolveconflict(_:).md)
- [func relinquishPresentedItem(toReader: ((() -> Void)?) -> Void)](nsdocument/relinquishpresenteditem(toreader:).md)
- [func savePresentedItemChanges(completionHandler: ((any Error)?) -> Void)](nsdocument/savepresenteditemchanges(completionhandler:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/relinquishpresenteditem(towriter:))*