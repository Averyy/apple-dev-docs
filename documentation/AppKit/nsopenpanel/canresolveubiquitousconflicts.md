# canResolveUbiquitousConflicts

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates how the panel responds to iCloud documents that have conflicting versions.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var canResolveUbiquitousConflicts: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), and the user attempts to open one or more documents with conflicts, the panel displays the conflict resolution UI. The user must resolve any conflicts before opening the documents. When the value of this property is [`false`](https://developer.apple.com/documentation/Swift/false), the your application is responsible for handling any conflicts.

The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), except for applications linked against the OS X v10.9 SDK or earlier that have adopted iCloud by specifying a ubiquitous container identifier entitlement.

For a better user experience, set this property to [`false`](https://developer.apple.com/documentation/Swift/false) and check the [`ubiquitousItemHasUnresolvedConflictsKey`](https://developer.apple.com/documentation/Foundation/URLResourceKey/ubiquitousItemHasUnresolvedConflictsKey) key of each item. When a conflict exists, retrieve a [`NSFileVersion`](https://developer.apple.com/documentation/Foundation/NSFileVersion) object for each version and present your own UI to resolve that conflict.

## See Also

- [var canDownloadUbiquitousContents: Bool](nsopenpanel/candownloadubiquitouscontents.md)
  A Boolean value that indicates how the panel responds to iCloud documents that aren’t fully downloaded locally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenpanel/canresolveubiquitousconflicts)*