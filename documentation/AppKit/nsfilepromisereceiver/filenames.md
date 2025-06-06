# fileNames

**Framework**: AppKit  
**Kind**: property

An array containing names of the promised files being written to the destination location.

**Availability**:
- macOS 10.12+

## Declaration

```swift
var fileNames: [String] { get }
```

#### Discussion

This property returns an empty array until the file promise is called using [`receivePromisedFiles(atDestination:options:operationQueue:reader:)`](nsfilepromisereceiver/receivepromisedfiles(atdestination:options:operationqueue:reader:).md).

## See Also

- [var fileTypes: [String]](nsfilepromisereceiver/filetypes.md)
  An array containing types of the promised files being written to the destination location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfilepromisereceiver/filenames)*