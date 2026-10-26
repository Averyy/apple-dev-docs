# data

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The data associated with a file.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var data: Data { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSData * data;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSData * data;
```

## See Also

### Getting the File Information
- [var filename: String](./filename.md)
  The name of the file.
- [var fileURL: URL?](./fileurl.md)
  The URL that describes the location of the file.
- [var typeIdentifier: String?](./typeidentifier.md)
  The type of the file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/infile/data)*