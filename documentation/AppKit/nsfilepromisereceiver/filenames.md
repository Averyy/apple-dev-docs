# fileNames

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array containing names of the promised files being written to the destination location.

**Availability**:
- macOS 10.12+

## Declaration

```swift
var fileNames: [String] { get }
```

```objc
@property (copy, readonly) NSArray<NSString *> * fileNames;
```

#### Discussion

This property returns an empty array until the file promise is called using [`receivePromisedFiles(atDestination:options:operationQueue:reader:)`](./receivepromisedfiles%28atdestination,options,operationqueue,reader%29.md).

## See Also

### Instance Properties
- [var fileTypes: [String]](./filetypes.md)
  An array containing types of the promised files being written to the destination location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfilepromisereceiver/filenames)*