# data

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A data object that contains the movie file’s data.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var data: Data? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSData * data;
```

## Discussion

The value is `nil` if you didn’t initialize the movie with data.

## See Also

### Accessing movie information
- [var url: URL?](./url.md)
  A URL to a QuickTime or ISO base media file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmovie/data)*