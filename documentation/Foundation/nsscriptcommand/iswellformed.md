# isWellFormed

**Framework**: Foundation  
**Kind**: property

Returns a Boolean value indicating whether the receiver is well formed according to its command description.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var isWellFormed: Bool { get }
```

#### Discussion

The method ensures that there is a description of the command and that the number of arguments and the types of non-specifier arguments conform to the command description.

## See Also

- [var commandDescription: NSScriptCommandDescription](nsscriptcommand/commanddescription.md)
  Returns the command description for the command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptcommand/iswellformed)*