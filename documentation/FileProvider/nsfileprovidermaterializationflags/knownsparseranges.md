# knownSparseRanges

**Framework**: File Provider  
**Kind**: property

A flag indicating that the system should consider the file fully materialized, even if it’s a sparse file.

**Availability**:
- macOS 12.3+

## Declaration

```swift
static var knownSparseRanges: NSFileProviderMaterializationFlags { get }
```

#### Discussion

There are two reasons why your app may pass a sparse file to the [`fetchPartialContents(for:version:request:minimalRange:aligningTo:options:completionHandler:)`](nsfileproviderpartialcontentfetching/fetchpartialcontents(for:version:request:minimalrange:aligningto:options:completionhandler:).md) method’s completion handler:

- You’re deliberately passing just part of the file to the completion handler, and the system should ignore anything outside your retrieved range.
- The original file contains sparse regions.

This flag tells the system that the original file deliberately has sparse ranges, and that the system can mark the file as materialized without having to request additional information. The system may use this information to optimize its requests, based on the system’s current state.

> ❗ **Important**:  Don’t use this flag unless the original file is a sparse file, and your file provider extension passed the entire file, including the sparse ranges, to the callback handler. Using this flag incorrectly may appear to work during testing, but may prevent the system from downloading complete files due to new performance improvements.

The system ignores this flag unless the retrieved range passed to the [`fetchPartialContents(for:version:request:minimalRange:aligningTo:options:completionHandler:)`](nsfileproviderpartialcontentfetching/fetchpartialcontents(for:version:request:minimalrange:aligningto:options:completionhandler:).md) method’s callback handler covers the entire file (a range with a location of zero and a length equal to the file-size in bytes).


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermaterializationflags/knownsparseranges)*