# standardError

**Framework**: Foundation  
**Kind**: property

The standard error stream.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var standardError: FileHandle? { get set }
```

#### Discussion

Setting to `nil` will bind the stream to `/dev/null`.

The default is `nil`.

## See Also

- [var standardInput: FileHandle?](nsuserunixtask/standardinput.md)
  The standard input stream.
- [var standardOutput: FileHandle?](nsuserunixtask/standardoutput.md)
  The standard output stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuserunixtask/standarderror)*