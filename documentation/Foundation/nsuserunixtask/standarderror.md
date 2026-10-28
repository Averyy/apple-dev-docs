# standardError

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The standard error stream.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var standardError: FileHandle? { get set }
```

```objc
@property (retain, nullable) NSFileHandle * standardError;
```

## Discussion

Setting to `nil` will bind the stream to `/dev/null`.

The default is `nil`.

## See Also

### Standard Unix Streams
- [var standardInput: FileHandle?](./standardinput.md)
  The standard input stream.
- [var standardOutput: FileHandle?](./standardoutput.md)
  The standard output stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuserunixtask/standarderror)*