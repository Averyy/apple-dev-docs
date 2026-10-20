# child

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Sets the receiver’s child reference.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
unowned(unsafe) var child: NSScriptObjectSpecifier? { get set }
```

```objc
@property (assign, nullable) NSScriptObjectSpecifier * childSpecifier;
```

#### Discussion

Do not invoke this method directly; it is automatically invoked by [`container`](./container.md).

## Parameters

- `child`: The receiver’s child reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/child)*