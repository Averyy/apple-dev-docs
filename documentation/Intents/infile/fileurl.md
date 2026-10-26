# fileURL

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The URL that describes the location of the file.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var fileURL: URL? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, strong, readonly, nullable) NSURL * fileURL;
```

*macOS*

```objc
@property (atomic, strong, readonly, nullable) NSURL * fileURL;
```

## See Also

### Getting the File Information
- [var filename: String](./filename.md)
  The name of the file.
- [var data: Data](./data.md)
  The data associated with a file.
- [var typeIdentifier: String?](./typeidentifier.md)
  The type of the file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/infile/fileurl)*