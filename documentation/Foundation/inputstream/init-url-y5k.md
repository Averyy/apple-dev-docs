# init(URL:)

**Framework**: Foundation  
**Kind**: init

Creates and returns an initialized `NSInputStream` object that reads data from the file at a given URL.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init?(URL url: URL)
```

#### Return Value

An initialized `NSInputStream` object that reads data from the URL at `url`.

#### Discussion

The stream must be opened before it can be used.

## Parameters

- `url`: The URL to the file.

## See Also

- [init(data: Data)](inputstream/init(data:).md)
  Initializes and returns an `NSInputStream` object for reading from a given `NSData` object.
- [convenience init?(fileAtPath: String)](inputstream/init(fileatpath:).md)
  Initializes and returns an `NSInputStream` object that reads data from the file at a given path.
- [init?(url: URL)](inputstream/init(url:)-1lfmj.md)
  Initializes and returns an `NSInputStream` object that reads data from the file at a given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/inputstream/init(url:)-y5k)*