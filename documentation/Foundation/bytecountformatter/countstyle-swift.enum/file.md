# ByteCountFormatter.CountStyle.file

**Framework**: Foundation  
**Kind**: case

Specifies display of file byte counts. The actual behavior for this is platform-specific; in macOS 10.8, this uses the decimal style, but that may change over time.

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
case file
```

## See Also

- [ByteCountFormatter.CountStyle.memory](bytecountformatter/countstyle-swift.enum/memory.md)
  Specifies display of memory byte counts. The actual behavior for this is platform-specific; in macOS 10.8, this uses the binary style, but that may change over time.
- [ByteCountFormatter.CountStyle.decimal](bytecountformatter/countstyle-swift.enum/decimal.md)
  Causes 1000 bytes to be shown as 1 KB. It is better to use [`ByteCountFormatter.CountStyle.file`](bytecountformatter/countstyle-swift.enum/file.md) or [`ByteCountFormatter.CountStyle.memory`](bytecountformatter/countstyle-swift.enum/memory.md) in most cases.
- [ByteCountFormatter.CountStyle.binary](bytecountformatter/countstyle-swift.enum/binary.md)
  Causes 1024 bytes to be shown as 1 KB. It is better to use [`ByteCountFormatter.CountStyle.file`](bytecountformatter/countstyle-swift.enum/file.md) or [`ByteCountFormatter.CountStyle.memory`](bytecountformatter/countstyle-swift.enum/memory.md) in most cases.
- [ByteCountFormatter.CountStyle.memory](bytecountformatter/countstyle-swift.enum/memory.md)
  Specifies display of memory byte counts. The actual behavior for this is platform-specific; in macOS 10.8, this uses the binary style, but that may change over time.
- [ByteCountFormatter.CountStyle.decimal](bytecountformatter/countstyle-swift.enum/decimal.md)
  Causes 1000 bytes to be shown as 1 KB. It is better to use [`ByteCountFormatter.CountStyle.file`](bytecountformatter/countstyle-swift.enum/file.md) or [`ByteCountFormatter.CountStyle.memory`](bytecountformatter/countstyle-swift.enum/memory.md) in most cases.
- [ByteCountFormatter.CountStyle.binary](bytecountformatter/countstyle-swift.enum/binary.md)
  Causes 1024 bytes to be shown as 1 KB. It is better to use [`ByteCountFormatter.CountStyle.file`](bytecountformatter/countstyle-swift.enum/file.md) or [`ByteCountFormatter.CountStyle.memory`](bytecountformatter/countstyle-swift.enum/memory.md) in most cases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bytecountformatter/countstyle-swift.enum/file)*