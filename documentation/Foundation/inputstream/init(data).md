# init(data:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes and returns an `NSInputStream` object for reading from a given `NSData` object.

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
init(data: Data)
```

```objc
- (instancetype) initWithData:(NSData *) data;
```

#### Return Value

An initialized `NSInputStream` object for reading from `data`.

#### Discussion

The stream must be opened before it can be used.

## Parameters

- `data`: The data object from which to read. The contents of `data` are copied.

## See Also

### Creating Streams
- [convenience init?(fileAtPath: String)](./init%28fileatpath%29.md)
  Initializes and returns an `NSInputStream` object that reads data from the file at a given path.
- [init?(url: URL)](./init%28url%29-1lfmj.md)
  Initializes and returns an `NSInputStream` object that reads data from the file at a given URL.
- [+ inputStreamWithFileAtPath:](../nsinputstream/inputstreamwithfileatpath_.md)
  Creates and returns an initialized `NSInputStream` object that reads data from the file at a given path.
### Related Documentation
- [+ inputStreamWithData:](../nsinputstream/inputstreamwithdata_.md)
  Creates and returns an initialized `NSInputStream` object for reading from a given `NSData` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/inputstream/init(data:))*