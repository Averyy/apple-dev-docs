# init(fileAtPath:)

**Framework**: Foundation  
**Kind**: init

Initializes and returns an `NSInputStream` object that reads data from the file at a given path.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init?(fileAtPath path: String)
```

#### Return Value

An initialized `NSInputStream` object that reads data from the file at `path`.

#### Discussion

The stream must be opened before it can be used.

## Parameters

- `path`: The path to the file.

## See Also

- [convenience init?(URL: URL)](inputstream/init(url:)-y5k.md)
  Creates and returns an initialized `NSInputStream` object that reads data from the file at a given URL.
- [convenience init?(URL: URL)](inputstream/init(url:)-y5k.md)
  Creates and returns an initialized `NSInputStream` object that reads data from the file at a given URL.
- [init(data: Data)](inputstream/init(data:).md)
  Initializes and returns an `NSInputStream` object for reading from a given `NSData` object.
- [init?(url: URL)](inputstream/init(url:)-1lfmj.md)
  Initializes and returns an `NSInputStream` object that reads data from the file at a given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/inputstream/init(fileatpath:))*