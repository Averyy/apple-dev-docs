# canDownloadUbiquitousContents

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates how the panel responds to iCloud documents that aren’t fully downloaded locally.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var canDownloadUbiquitousContents: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the panel disallows opening non-local iCloud files. If the user selects a non-local file, the panel attempts to download that file. When the value of this property is [`false`](https://developer.apple.com/documentation/swift/false), the user may select and open non-local files. Your app is responsible for downloading the files and reporting progress or any issues.

The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true), except for applications linked against the OS X v10.9 SDK or earlier that have adopted iCloud by specifying a ubiquitous container identifier entitlement.

For a better user experience, set this property to [`false`](https://developer.apple.com/documentation/swift/false) and download the file’s contents with an [`NSFileCoordinator`](https://developer.apple.com/documentation/Foundation/NSFileCoordinator) object. Show the dlownload progress using a [`Progress`](https://developer.apple.com/documentation/Foundation/Progress) or [`NSMetadataQuery`](https://developer.apple.com/documentation/Foundation/NSMetadataQuery) object.

## See Also

- [var canResolveUbiquitousConflicts: Bool](nsopenpanel/canresolveubiquitousconflicts.md)
  A Boolean value that indicates how the panel responds to iCloud documents that have conflicting versions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenpanel/candownloadubiquitouscontents)*