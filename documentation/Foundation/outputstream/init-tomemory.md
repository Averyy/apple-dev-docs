# init(toMemory:)

**Framework**: Foundation  
**Kind**: init

Returns an initialized output stream that will write to memory.

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
init(toMemory: ())
```

#### Return Value

An initialized output stream that will write stream data to memory.

#### Discussion

The stream must be opened before it can be used.

The contents of the memory stream are retrieved by passing the constant `NSStreamDataWrittenToMemoryStreamKey` to [`property(forKey:)`](stream/property(forkey:).md).

## See Also

- [class func toMemory() -> Self](outputstream/tomemory.md)
  Creates and returns an initialized output stream that will write stream data to memory.
- [convenience init?(URL: URL, append: Bool)](outputstream/init(url:append:)-8e5le.md)
  Creates and returns an initialized output stream for writing to a specified URL.
- [init(toBuffer: UnsafeMutablePointer<UInt8>, capacity: Int)](outputstream/init(tobuffer:capacity:).md)
  Returns an initialized output stream that can write to a provided buffer.
- [convenience init?(toFileAtPath: String, append: Bool)](outputstream/init(tofileatpath:append:).md)
  Returns an initialized output stream for writing to a specified file.
- [init?(url: URL, append: Bool)](outputstream/init(url:append:)-5soau.md)
  Returns an initialized output stream for writing to a specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/outputstream/init(tomemory:))*