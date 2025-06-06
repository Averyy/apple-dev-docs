# standardOutput

**Framework**: Foundation  
**Kind**: property

The standard output stream.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var standardOutput: FileHandle? { get set }
```

#### Discussion

Setting to `nil` will bind the stream to `/dev/null`.

The default is `nil`.

## See Also

- [var standardError: FileHandle?](nsuserunixtask/standarderror.md)
  The standard error stream.
- [var standardInput: FileHandle?](nsuserunixtask/standardinput.md)
  The standard input stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuserunixtask/standardoutput)*