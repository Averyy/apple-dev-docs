# standardInput

**Framework**: Foundation  
**Kind**: property

The standard input stream.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var standardInput: FileHandle? { get set }
```

#### Discussion

Setting to `nil` will bind the stream to `/dev/null`.

The default is `nil`.

## See Also

- [var standardError: FileHandle?](nsuserunixtask/standarderror.md)
  The standard error stream.
- [var standardOutput: FileHandle?](nsuserunixtask/standardoutput.md)
  The standard output stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuserunixtask/standardinput)*