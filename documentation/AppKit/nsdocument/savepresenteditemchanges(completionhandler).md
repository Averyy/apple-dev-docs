# savePresentedItemChanges(completionHandler:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 10.7+

## Declaration

```swift
nonisolated
func savePresentedItemChanges(completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
nonisolated
func savePresentedItemChanges() async throws
```

```objc
- (void) savePresentedItemChangesWithCompletionHandler:(void (^)(NSError *errorOrNil)) completionHandler;
```

## Discussion

## See Also

### Instance Methods
- [func accommodatePresentedItemDeletion(completionHandler: ((any Error)?) -> Void)](./accommodatepresenteditemdeletion%28completionhandler%29.md)
- [func presentedItemDidChange()](./presenteditemdidchange%28%29.md)
- [func presentedItemDidChangeUbiquityAttributes(Set<URLResourceKey>)](./presenteditemdidchangeubiquityattributes%28_%29.md)
- [func presentedItemDidGain(NSFileVersion)](./presenteditemdidgain%28_%29.md)
- [func presentedItemDidLose(NSFileVersion)](./presenteditemdidlose%28_%29.md)
- [func presentedItemDidMove(to: URL)](./presenteditemdidmove%28to%29.md)
- [func presentedItemDidResolveConflict(NSFileVersion)](./presenteditemdidresolveconflict%28_%29.md)
- [func relinquishPresentedItem(toReader: ((() -> Void)?) -> Void)](./relinquishpresenteditem%28toreader%29.md)
- [func relinquishPresentedItem(toWriter: ((() -> Void)?) -> Void)](./relinquishpresenteditem%28towriter%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/savepresenteditemchanges(completionhandler:))*