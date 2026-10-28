# fileTypes

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array containing types of the promised files being written to the destination location.

**Availability**:
- macOS 10.12+

## Declaration

```swift
var fileTypes: [String] { get }
```

```objc
@property (copy, readonly) NSArray<NSString *> * fileTypes;
```

## Discussion

[`NSFilePromiseProvider`](../nsfilepromiseprovider.md) promises one file type per item. The `count` of `fileTypes` should tell you the number of promised files in this item, but that’s not always guaranteed. Some legacy file promisers  list each unique `fileType` only once.

## See Also

### Instance Properties
- [var fileNames: [String]](./filenames.md)
  An array containing names of the promised files being written to the destination location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfilepromisereceiver/filetypes)*