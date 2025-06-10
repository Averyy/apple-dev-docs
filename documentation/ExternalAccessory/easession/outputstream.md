# outputStream

**Framework**: External Accessory  
**Kind**: property

The stream to use for sending data to the accessory.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var outputStream: OutputStream? { get }
```

#### Discussion

This stream is provided for you automatically by the session object but you must configure it if you want to receive any associated stream events. You do this by assigning a delegate object to the stream that implements the [`stream(_:handle:)`](https://developer.apple.com/documentation/Foundation/StreamDelegate/stream(_:handle:)) delegate method. You must then schedule the stream in a run loop so that it can send data asynchronously from one of your application’s threads.

For more information on how to schedule an output stream in a run loop and use it to send data, see [`Stream Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Streams/Streams.html#//apple_ref/doc/uid/10000188i).

## See Also

- [var inputStream: InputStream?](easession/inputstream.md)
  The stream to use for receiving data from the accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/easession/outputstream)*