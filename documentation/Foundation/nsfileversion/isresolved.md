# isResolved

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates the version object is not in conflict ([`true`](https://developer.apple.com/documentation/swift/true)) or is in conflict ([`false`](https://developer.apple.com/documentation/swift/false)).

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
var isResolved: Bool { get set }
```

#### Discussion

When the system detects a conflict involving versions of a file, it sets this property to [`false`](https://developer.apple.com/documentation/swift/false) to indicate an unresolved conflict. After you resolve the conflict, set this property to [`true`](https://developer.apple.com/documentation/swift/true) to tell the system it is resolved; you must then remove any versions of the file that are no longer useful.

> ❗ **Important**:  If you do not explicitly remove versions of a file that are no longer useful, iCloud continues to sync them to all a user’s devices and those versions continue to consume user iCloud quota.

 If you do not explicitly remove versions of a file that are no longer useful, iCloud continues to sync them to all a user’s devices and those versions continue to consume user iCloud quota.

To remove an unused version of a file, call the [`remove()`](nsfileversion/remove().md) method. To remove all unused versions of a file, call the [`removeOtherVersionsOfItem(at:)`](nsfileversion/removeotherversionsofitem(at:).md) method.

> ❗ **Important**:  Never set the value of this property to [`false`](https://developer.apple.com/documentation/swift/false). If you do, the system raises an exception.

 Never set the value of this property to [`false`](https://developer.apple.com/documentation/swift/false). If you do, the system raises an exception.

Resolving a conflict causes the file version object to be removed from any reports about conflicting versions, such as those returned by the [`unresolvedConflictVersionsOfItem(at:)`](nsfileversion/unresolvedconflictversionsofitem(at:).md) method.

## See Also

- [var isConflict: Bool](nsfileversion/isconflict.md)
  A Boolean value indicating whether the contents of the version are in conflict with the contents of another version.
- [class func unresolvedConflictVersionsOfItem(at: URL) -> [NSFileVersion]?](nsfileversion/unresolvedconflictversionsofitem(at:).md)
  Returns an array of version objects that are currently in conflict for the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfileversion/isresolved)*