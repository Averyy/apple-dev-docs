# arguments

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Sets the arguments of the command to `args`.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var arguments: [String : Any]? { get set }
```

```objc
@property (copy, nullable) NSDictionary<NSString *,id> * arguments;
```

#### Discussion

Each argument in the dictionary is identified by the same name key used for the argument in the command’s class declaration in the script suite file.

## See Also

### Accessing arguments
- [var evaluatedArguments: [String : Any]?](./evaluatedarguments.md)
  Returns a dictionary containing the arguments of the command, evaluated from object specifiers to objects if necessary. The keys in the dictionary are the argument names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptcommand/arguments)*