# allowAccessingOriginalFile

**Framework**: Core Transferable  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the receiver can read and write the original file. When set to `false`, the receiver can only gain access to a copy of the file.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
let allowAccessingOriginalFile: Bool
```

## See Also

### Configuring a file transfer
- [init(URL, allowAccessingOriginalFile: Bool)](./init%28_,allowaccessingoriginalfile%29.md)
  Creates a description of a file from the perspective of the sender.
- [let file: URL](./file.md)
  A URL that describes the location of the file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretransferable/senttransferredfile/allowaccessingoriginalfile)*