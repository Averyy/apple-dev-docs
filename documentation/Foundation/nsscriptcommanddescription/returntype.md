# returnType

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the return type of the command.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var returnType: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * returnType;
```

#### Return Value

The receiver’s command return type; for example, `"NSNumber"` or `"NSDictionary"`).

## See Also

### Getting Command Return-Type Information
- [var appleEventCodeForReturnType: FourCharCode](./appleeventcodeforreturntype.md)
  Returns the Apple event code that identifies the command’s return type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/returntype)*