# appleEventCodeForArgument(withName:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the Apple event code for the specified command argument of the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func appleEventCodeForArgument(withName argumentName: String) -> FourCharCode
```

```objc
- (FourCharCode) appleEventCodeForArgumentWithName:(NSString *) argumentName;
```

## Return Value

The code for the specified argument.

## Parameters

- `argumentName`: The argument name (used as a key) for which to obtain the corresponding Apple event code.

## See Also

### Getting Command Argument Information
- [var argumentNames: [String]](./argumentnames.md)
  Returns the names (or keys) for all arguments of the receiver’s command.
- [func isOptionalArgument(withName: String) -> Bool](./isoptionalargument%28withname%29.md)
  Returns a Boolean value that indicates whether the command argument identified by the specified argument key is an optional argument.
- [func typeForArgument(withName: String) -> String?](./typeforargument%28withname%29.md)
  Returns the type of the command argument identified by the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/appleeventcodeforargument(withname:))*