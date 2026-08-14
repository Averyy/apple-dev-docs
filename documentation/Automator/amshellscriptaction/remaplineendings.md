# remapLineEndings

**Framework**: Automator  
**Kind**: property

A Boolean value that indicates whether you want automatic remapping of carriage return (`\r`) to newline (`\n`) characters in the input string.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
var remapLineEndings: Bool { get }
```

#### Discussion

The default is [`false`](https://developer.apple.com/documentation/swift/false). Override to return [`true`](https://developer.apple.com/documentation/swift/true) if you want the remapping to occur.

## See Also

- [var inputFieldSeparator: String](amshellscriptaction/inputfieldseparator.md)
  A string to use as the delimiter between items in the string passed to the action through standard input.
- [var outputFieldSeparator: String](amshellscriptaction/outputfieldseparator.md)
  A string to use as a delimiter in the string output by the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amshellscriptaction/remaplineendings)*