# canDownloadUbiquitousContents

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates how the panel responds to iCloud documents that aren’t fully downloaded locally.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var canDownloadUbiquitousContents: Bool { get set }
```

```objc
@property BOOL canDownloadUbiquitousContents;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the panel disallows opening non-local iCloud files. If the user selects a non-local file, the panel attempts to download that file. When the value of this property is [`false`](../../Swift/false.md), the user may select and open non-local files. Your app is responsible for downloading the files and reporting progress or any issues.

The default value of this property is [`true`](../../Swift/true.md), except for applications linked against the OS X v10.9 SDK or earlier that have adopted iCloud by specifying a ubiquitous container identifier entitlement.

For a better user experience, set this property to [`false`](../../Swift/false.md) and download the file’s contents with an [`NSFileCoordinator`](../../Foundation/nsfilecoordinator.md) object. Show the dlownload progress using a [`Progress`](../../Foundation/progress.md) or [`NSMetadataQuery`](../../Foundation/nsmetadataquery.md) object.

## See Also

### Supporting iCloud Documents
- [var canResolveUbiquitousConflicts: Bool](./canresolveubiquitousconflicts.md)
  A Boolean value that indicates how the panel responds to iCloud documents that have conflicting versions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenpanel/candownloadubiquitouscontents)*