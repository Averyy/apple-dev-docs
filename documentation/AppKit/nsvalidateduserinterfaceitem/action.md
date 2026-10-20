# action

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Returns the selector of the receiver’s action method.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
var action: Selector? { get }
```

```objc
@property (readonly, nullable) SEL action;
```

#### Return Value

The selector of the receiver’s action method.

## See Also

### Related Documentation
- [User Interface Validation](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/UIValidation/UIValidation.html#//apple_ref/doc/uid/10000040i)
### Getting information about a user interface item
- [var tag: Int](./tag.md)
  Returns the receiver’s tag integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsvalidateduserinterfaceitem/action)*