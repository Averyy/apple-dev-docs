# outputStreamWithURL:append:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns an initialized output stream for writing to a specified URL.

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
+ (instancetype) outputStreamWithURL:(NSURL *) url append:(BOOL) shouldAppend;
```

#### Discussion

The stream must be opened before it can be used.

## Parameters

- `url`: The URL to the file the output stream will write to.
- `shouldAppend`: `YES` if newly written data should be appended to any existing file contents, otherwise `NO`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsoutputstream/outputstreamwithurl:append:)*