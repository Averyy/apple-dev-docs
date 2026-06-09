# init(dataItem:)

**Framework**: Foundation  
**Kind**: init

Creates a message that indicates a file handle reached the end of a file or the data.

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
init(dataItem: Result<Data, POSIXError>)
```

## Parameters

- `dataItem`: A result instance that contains either the data read in or an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/readtoendoffilecompletionmessage/init(dataitem:))*