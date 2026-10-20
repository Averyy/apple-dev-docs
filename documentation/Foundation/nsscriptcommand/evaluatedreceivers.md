# evaluatedReceivers

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the object or objects to which the command is to be sent (called both the “receivers” or “targets” of script commands).

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var evaluatedReceivers: Any? { get }
```

```objc
@property (retain, readonly, nullable) id evaluatedReceivers;
```

#### Discussion

It evaluates receivers, which are always object specifiers, to a proper object. If the command does not specify a receiver, or if the receiver doesn’t accept the command, it returns `nil`.

## See Also

### Accessing receivers
- [var receiversSpecifier: NSScriptObjectSpecifier?](./receiversspecifier.md)
  Sets the object specifier to `receiversSpec` that, when evaluated, indicates the receiver or receivers of the command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptcommand/evaluatedreceivers)*