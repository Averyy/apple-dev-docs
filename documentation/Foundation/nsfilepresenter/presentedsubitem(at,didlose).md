# presentedSubitem(at:didLose:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the item inside the presented directory lost an existing version.

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
optional func presentedSubitem(at url: URL, didLose version: NSFileVersion)
```

```objc
- (void) presentedSubitemAtURL:(NSURL *) url didLoseVersion:(NSFileVersion *) version;
```

#### Discussion

Your delegate can use this method to determine how to handle the loss of the specified file version. For an old version, you might not have to do anything. However, if your application is currently using the lost version, you would need to update your application’s user interface or prompt the user about how to proceed.

## Parameters

- `url`: The URL of the item inside the presented directory that lost a version. The item need not be at the top level of the presented directory but may itself be inside a nested subdirectory.
- `version`: The file version object containing information about the version that was removed.

## See Also

### Responding to Version Changes
- [func presentedItemDidGain(NSFileVersion)](./presenteditemdidgain%28_%29.md)
  Tells the delegate that a new version of the file or file package was added.
- [func presentedItemDidLose(NSFileVersion)](./presenteditemdidlose%28_%29.md)
  Tells the delegate that a version of the file or file package was removed.
- [func presentedItemDidResolveConflict(NSFileVersion)](./presenteditemdidresolveconflict%28_%29.md)
  Tells the delegate that some other entity resolved a version conflict for the presenter’s file or file package.
- [func presentedSubitem(at: URL, didGain: NSFileVersion)](./presentedsubitem%28at,didgain%29.md)
  Tells the delegate that the item inside the presented directory gained a new version.
- [func presentedSubitem(at: URL, didResolve: NSFileVersion)](./presentedsubitem%28at,didresolve%29.md)
  Tells the delegate that the item inside the presented directory had a version conflict resolved by an outside entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilepresenter/presentedsubitem(at:didlose:))*