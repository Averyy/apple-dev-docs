# init(url:append:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns an initialized output stream for writing to a specified URL.

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
init?(url: URL, append shouldAppend: Bool)
```

```objc
- (instancetype) initWithURL:(NSURL *) url append:(BOOL) shouldAppend;
```

#### Return Value

An initialized output stream that can write to `url`.

#### Discussion

The stream must be opened before it can be used.

## Parameters

- `url`: The URL to the file the output stream will write to.
- `shouldAppend`: [`true`](../../Swift/true.md) if newly written data should be appended to any existing file contents, otherwise [`false`](../../Swift/false.md).

## See Also

### Creating Streams
- [class func toMemory() -> Self](./tomemory%28%29.md)
  Creates and returns an initialized output stream that will write stream data to memory.
- [init(toMemory: ())](./init%28tomemory%29.md)
  Returns an initialized output stream that will write to memory.
- [init(toBuffer: UnsafeMutablePointer<UInt8>, capacity: Int)](./init%28tobuffer,capacity%29.md)
  Returns an initialized output stream that can write to a provided buffer.
- [convenience init?(toFileAtPath: String, append: Bool)](./init%28tofileatpath,append%29.md)
  Returns an initialized output stream for writing to a specified file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/outputstream/init(url:append:)-5soau)*