# init(url:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes and returns an `NSInputStream` object that reads data from the file at a given URL.

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
init?(url: URL)
```

```objc
- (instancetype) initWithURL:(NSURL *) url;
```

## Return Value

An initialized `NSInputStream` object that reads data from the file at `url`.

## Discussion

The stream must be opened before it can be used.

## Parameters

- `url`: The URL to the file.

## See Also

### Creating Streams
- [init(data: Data)](./init%28data%29.md)
  Initializes and returns an `NSInputStream` object for reading from a given `NSData` object.
- [convenience init?(fileAtPath: String)](./init%28fileatpath%29.md)
  Initializes and returns an `NSInputStream` object that reads data from the file at a given path.
- [+ inputStreamWithData:](../nsinputstream/inputstreamwithdata_.md)
  Creates and returns an initialized `NSInputStream` object for reading from a given `NSData` object.
- [+ inputStreamWithFileAtPath:](../nsinputstream/inputstreamwithfileatpath_.md)
  Creates and returns an initialized `NSInputStream` object that reads data from the file at a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/inputstream/init(url:)-1lfmj)*