# init(fileAtPath:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithFileAtPath:(NSString *) path;
```

#### Return Value

An initialized `NSInputStream` object that reads data from the file at `path`.

#### Discussion

The stream must be opened before it can be used.

## Parameters

- `path`: The path to the file.

## See Also

### Creating Streams
- [init(data: Data)](./init%28data%29.md)
  Initializes and returns an `NSInputStream` object for reading from a given `NSData` object.
- [init?(url: URL)](./init%28url%29-1lfmj.md)
  Initializes and returns an `NSInputStream` object that reads data from the file at a given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/inputstream/init(fileatpath:))*