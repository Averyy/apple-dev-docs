# commandDescription

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the command description for the command.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var commandDescription: NSScriptCommandDescription { get }
```

```objc
@property (retain, readonly) NSScriptCommandDescription * commandDescription;
```

## Discussion

Once a command is created, its command description is immutable.

## See Also

### Related Documentation
- [var isWellFormed: Bool](./iswellformed.md)
  Returns a Boolean value indicating whether the receiver is well formed according to its command description.
### Getting command information
- [var isWellFormed: Bool](./iswellformed.md)
  Returns a Boolean value indicating whether the receiver is well formed according to its command description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptcommand/commanddescription)*