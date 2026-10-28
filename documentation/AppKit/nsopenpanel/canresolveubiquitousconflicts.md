# canResolveUbiquitousConflicts

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates how the panel responds to iCloud documents that have conflicting versions.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var canResolveUbiquitousConflicts: Bool { get set }
```

```objc
@property BOOL canResolveUbiquitousConflicts;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), and the user attempts to open one or more documents with conflicts, the panel displays the conflict resolution UI. The user must resolve any conflicts before opening the documents. When the value of this property is [`false`](../../Swift/false.md), the your application is responsible for handling any conflicts.

The default value of this property is [`true`](../../Swift/true.md), except for applications linked against the OS X v10.9 SDK or earlier that have adopted iCloud by specifying a ubiquitous container identifier entitlement.

For a better user experience, set this property to [`false`](../../Swift/false.md) and check the [`ubiquitousItemHasUnresolvedConflictsKey`](../../Foundation/urlresourcekey/ubiquitousitemhasunresolvedconflictskey.md) key of each item. When a conflict exists, retrieve a [`NSFileVersion`](../../Foundation/nsfileversion.md) object for each version and present your own UI to resolve that conflict.

## See Also

### Supporting iCloud Documents
- [var canDownloadUbiquitousContents: Bool](./candownloadubiquitouscontents.md)
  A Boolean value that indicates how the panel responds to iCloud documents that aren’t fully downloaded locally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenpanel/canresolveubiquitousconflicts)*