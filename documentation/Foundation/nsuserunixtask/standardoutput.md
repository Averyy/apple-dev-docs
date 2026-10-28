# standardOutput

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The standard output stream.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var standardOutput: FileHandle? { get set }
```

```objc
@property (retain, nullable) NSFileHandle * standardOutput;
```

## Discussion

Setting to `nil` will bind the stream to `/dev/null`.

The default is `nil`.

## See Also

### Standard Unix Streams
- [var standardError: FileHandle?](./standarderror.md)
  The standard error stream.
- [var standardInput: FileHandle?](./standardinput.md)
  The standard input stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuserunixtask/standardoutput)*