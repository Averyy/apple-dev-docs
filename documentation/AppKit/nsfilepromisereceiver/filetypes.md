# fileTypes

**Framework**: AppKit  
**Kind**: property

An array containing types of the promised files being written to the destination location.

**Availability**:
- macOS 10.12+

## Declaration

```swift
var fileTypes: [String] { get }
```

#### Discussion

[`NSFilePromiseProvider`](nsfilepromiseprovider.md) promises one file type per item. The `count` of `fileTypes` should tell you the number of promised files in this item, but that’s not always guaranteed. Some legacy file promisers  list each unique `fileType` only once.

## See Also

- [var fileNames: [String]](nsfilepromisereceiver/filenames.md)
  An array containing names of the promised files being written to the destination location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfilepromisereceiver/filetypes)*