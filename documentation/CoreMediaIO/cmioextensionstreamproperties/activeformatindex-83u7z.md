# activeFormatIndex

**Framework**: Core Media I/O  
**Kind**: property

The index of the active format.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+
- Xcode 13.0+

## Declaration

```swift
@nonobjc
var activeFormatIndex: Int? { get set }
```

#### Discussion

This value represents the index of the active format in the source’s [`formats`](cmioextensionstreamsource/formats.md) array.

The key for this property is [`streamActiveFormatIndex`](cmioextensionproperty/streamactiveformatindex.md).

## See Also

- [var frameDuration: CMTime?](cmioextensionstreamproperties/frameduration-4rnl9.md)
  The duration of the frame.
- [var maxFrameDuration: CMTime?](cmioextensionstreamproperties/maxframeduration-5qqg.md)
  The maximum duration of a frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamproperties/activeformatindex-83u7z)*