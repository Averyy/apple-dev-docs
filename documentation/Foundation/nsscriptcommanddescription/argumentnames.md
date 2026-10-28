# argumentNames

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the names (or keys) for all arguments of the receiver’s command.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var argumentNames: [String] { get }
```

```objc
@property (copy, readonly) NSArray<NSString *> * argumentNames;
```

## Return Value

The array of argument names. If there are no arguments for the command, returns an empty array.

## See Also

### Getting Command Argument Information
- [func appleEventCodeForArgument(withName: String) -> FourCharCode](./appleeventcodeforargument%28withname%29.md)
  Returns the Apple event code for the specified command argument of the receiver.
- [func isOptionalArgument(withName: String) -> Bool](./isoptionalargument%28withname%29.md)
  Returns a Boolean value that indicates whether the command argument identified by the specified argument key is an optional argument.
- [func typeForArgument(withName: String) -> String?](./typeforargument%28withname%29.md)
  Returns the type of the command argument identified by the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/argumentnames)*