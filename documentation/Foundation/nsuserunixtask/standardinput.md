# standardInput

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The standard input stream.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var standardInput: FileHandle? { get set }
```

```objc
@property (retain, nullable) NSFileHandle * standardInput;
```

#### Discussion

Setting to `nil` will bind the stream to `/dev/null`.

The default is `nil`.

## See Also

### Standard Unix Streams
- [var standardError: FileHandle?](./standarderror.md)
  The standard error stream.
- [var standardOutput: FileHandle?](./standardoutput.md)
  The standard output stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuserunixtask/standardinput)*