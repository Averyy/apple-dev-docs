# isOptionalArgument(withName:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value that indicates whether the command argument identified by the specified argument key is an optional argument.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func isOptionalArgument(withName argumentName: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the specified argument exists and is optional; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `argumentName`: Argument name (used as a key) that identifies the command argument to examine.

## See Also

- [func appleEventCodeForArgument(withName: String) -> FourCharCode](nsscriptcommanddescription/appleeventcodeforargument(withname:).md)
  Returns the Apple event code for the specified command argument of the receiver.
- [var argumentNames: [String]](nsscriptcommanddescription/argumentnames.md)
  Returns the names (or keys) for all arguments of the receiver’s command.
- [func typeForArgument(withName: String) -> String?](nsscriptcommanddescription/typeforargument(withname:).md)
  Returns the type of the command argument identified by the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/isoptionalargument(withname:))*