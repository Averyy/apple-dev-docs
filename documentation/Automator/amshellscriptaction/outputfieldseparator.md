# outputFieldSeparator

**Framework**: Automator  
**Kind**: property

A string to use as a delimiter in the string output by the action.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
var outputFieldSeparator: String { get }
```

#### Discussion

Upon completion, the Automator framework converts an output string provided by the action into an array (or list), to be passed to the next action in the workflow for further processing. The elements in this array are derived from fields delimited by the output field separator. The default value is the separator character returned by [`inputFieldSeparator`](amshellscriptaction/inputfieldseparator.md). Override this method if you want a different delimiter for output.

## See Also

- [var inputFieldSeparator: String](amshellscriptaction/inputfieldseparator.md)
  A string to use as the delimiter between items in the string passed to the action through standard input.
- [var remapLineEndings: Bool](amshellscriptaction/remaplineendings.md)
  A Boolean value that indicates whether you want automatic remapping of carriage return (`\r`) to newline (`\n`) characters in the input string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amshellscriptaction/outputfieldseparator)*