# init(toFileAtPath:append:)

**Framework**: Foundation  
**Kind**: init

Returns an initialized output stream for writing to a specified file.

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
convenience init?(toFileAtPath path: String, append shouldAppend: Bool)
```

#### Return Value

An initialized output stream that can write to `path`.

#### Discussion

The stream must be opened before it can be used.

## Parameters

- `path`: The path to the file the output stream will write to.
- `shouldAppend`:   if newly written data should be appended to any existing file contents, otherwise  .

## See Also

- [convenience init?(URL: URL, append: Bool)](outputstream/init(url:append:)-8e5le.md)
  Creates and returns an initialized output stream for writing to a specified URL.
- [class func toMemory() -> Self](outputstream/tomemory.md)
  Creates and returns an initialized output stream that will write stream data to memory.
- [convenience init?(URL: URL, append: Bool)](outputstream/init(url:append:)-8e5le.md)
  Creates and returns an initialized output stream for writing to a specified URL.
- [init(toMemory: ())](outputstream/init(tomemory:).md)
  Returns an initialized output stream that will write to memory.
- [init(toBuffer: UnsafeMutablePointer<UInt8>, capacity: Int)](outputstream/init(tobuffer:capacity:).md)
  Returns an initialized output stream that can write to a provided buffer.
- [init?(url: URL, append: Bool)](outputstream/init(url:append:)-5soau.md)
  Returns an initialized output stream for writing to a specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/outputstream/init(tofileatpath:append:))*