# inputStreamWithData:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns an initialized `NSInputStream` object for reading from a given `NSData` object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (instancetype) inputStreamWithData:(NSData *) data;
```

## Return Value

An initialized `NSInputStream` object for reading from `data`. If `data` is not an NSData object, this method returns `nil`.

## Discussion

The stream must be opened before it can be used.

## Parameters

- `data`: The data object from which to read. The contents of `data` are copied.

## See Also

### Related Documentation
- [Stream Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Streams/Streams.html#//apple_ref/doc/uid/10000188i)
### Creating Streams
- [+ inputStreamWithFileAtPath:](./inputstreamwithfileatpath_.md)
  Creates and returns an initialized `NSInputStream` object that reads data from the file at a given path.
- [init(data: Data)](../inputstream/init%28data%29.md)
  Initializes and returns an `NSInputStream` object for reading from a given `NSData` object.
- [convenience init?(fileAtPath: String)](../inputstream/init%28fileatpath%29.md)
  Initializes and returns an `NSInputStream` object that reads data from the file at a given path.
- [init?(url: URL)](../inputstream/init%28url%29-1lfmj.md)
  Initializes and returns an `NSInputStream` object that reads data from the file at a given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsinputstream/inputstreamwithdata:)*