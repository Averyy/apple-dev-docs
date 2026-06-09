# init(fileHandleItem:)

**Framework**: Foundation  
**Kind**: init

Creates a message for a file handle connection acceptance.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init(fileHandleItem: Result<FileHandle, POSIXError>)
```

## Parameters

- `fileHandleItem`: A result instance containing either the file handle representing the “near” end of a socket connection, or an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/connectionacceptedmessage/init(filehandleitem:))*