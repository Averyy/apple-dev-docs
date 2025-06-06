# arguments

**Framework**: Foundation  
**Kind**: property

Sets the arguments of the command to `args`.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var arguments: [String : Any]? { get set }
```

#### Discussion

Each argument in the dictionary is identified by the same name key used for the argument in the command’s class declaration in the script suite file.

## See Also

- [var evaluatedArguments: [String : Any]?](nsscriptcommand/evaluatedarguments.md)
  Returns a dictionary containing the arguments of the command, evaluated from object specifiers to objects if necessary. The keys in the dictionary are the argument names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptcommand/arguments)*