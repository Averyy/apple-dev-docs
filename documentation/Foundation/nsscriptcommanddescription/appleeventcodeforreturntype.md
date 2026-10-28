# appleEventCodeForReturnType

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the Apple event code that identifies the command’s return type.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var appleEventCodeForReturnType: FourCharCode { get }
```

```objc
@property (readonly) FourCharCode appleEventCodeForReturnType;
```

## Return Value

The event code for the command’s return type.

## See Also

### Related Documentation
- [func appleEventCodeForArgument(withName: String) -> FourCharCode](./appleeventcodeforargument%28withname%29.md)
  Returns the Apple event code for the specified command argument of the receiver.
### Getting Command Return-Type Information
- [var returnType: String?](./returntype.md)
  Returns the return type of the command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/appleeventcodeforreturntype)*