# inputStreamWithURL:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (instancetype) inputStreamWithURL:(NSURL *) url;
```

## Discussion

The stream must be opened before it can be used.

## Parameters

- `url`: The URL to the file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsinputstream/inputstreamwithurl:)*