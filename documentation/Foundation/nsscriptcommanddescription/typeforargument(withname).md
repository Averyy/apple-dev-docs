# typeForArgument(withName:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the type of the command argument identified by the specified key.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func typeForArgument(withName argumentName: String) -> String?
```

```objc
- (NSString *) typeForArgumentWithName:(NSString *) argumentName;
```

#### Return Value

The type of the specified command argument. Returns `nil` if there is no such argument.

## Parameters

- `argumentName`: Argument name (used as a key) that identifies the command argument to examine.

## See Also

### Getting Command Argument Information
- [func appleEventCodeForArgument(withName: String) -> FourCharCode](./appleeventcodeforargument%28withname%29.md)
  Returns the Apple event code for the specified command argument of the receiver.
- [var argumentNames: [String]](./argumentnames.md)
  Returns the names (or keys) for all arguments of the receiver’s command.
- [func isOptionalArgument(withName: String) -> Bool](./isoptionalargument%28withname%29.md)
  Returns a Boolean value that indicates whether the command argument identified by the specified argument key is an optional argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/typeforargument(withname:))*