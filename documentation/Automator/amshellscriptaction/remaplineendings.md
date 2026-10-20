# remapLineEndings

**Framework**: Automator  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether you want automatic remapping of carriage return (`\r`) to newline (`\n`) characters in the input string.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
var remapLineEndings: Bool { get }
```

```objc
@property (atomic, readonly) BOOL remapLineEndings;
```

#### Discussion

The default is [`false`](../../Swift/false.md). Override to return [`true`](../../Swift/true.md) if you want the remapping to occur.

## See Also

### Handling the I/O Separator Character
- [var inputFieldSeparator: String](./inputfieldseparator.md)
  A string to use as the delimiter between items in the string passed to the action through standard input.
- [var outputFieldSeparator: String](./outputfieldseparator.md)
  A string to use as a delimiter in the string output by the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amshellscriptaction/remaplineendings)*