# init(URL:append:)

**Framework**: Foundation  
**Kind**: init

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

```swift
convenience init?(URL url: URL, append shouldAppend: Bool)
```

#### Return Value

An initialized output stream that can write to `url`.

#### Discussion

The stream must be opened before it can be used.

## Parameters

- `url`: The URL to the file the output stream will write to.
- `shouldAppend`:   if newly written data should be appended to any existing file contents, otherwise  .

## See Also

- [class func toMemory() -> Self](outputstream/tomemory.md)
  Creates and returns an initialized output stream that will write stream data to memory.
- [init(toMemory: ())](outputstream/init(tomemory:).md)
  Returns an initialized output stream that will write to memory.
- [init(toBuffer: UnsafeMutablePointer<UInt8>, capacity: Int)](outputstream/init(tobuffer:capacity:).md)
  Returns an initialized output stream that can write to a provided buffer.
- [convenience init?(toFileAtPath: String, append: Bool)](outputstream/init(tofileatpath:append:).md)
  Returns an initialized output stream for writing to a specified file.
- [init?(url: URL, append: Bool)](outputstream/init(url:append:)-5soau.md)
  Returns an initialized output stream for writing to a specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/outputstream/init(url:append:)-8e5le)*