# init(identifier:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Performs default initialization for the receiver.

**Availability**:
- macOS

## Declaration

```swift
init(identifier: Any?)
```

```objc
- (instancetype) initWithIdentifier:(id) identifier;
```

## Discussion

Sets the receiver’s identifier object to `identifier`, if it is not `nil`. Use this method when creating tab view items programmatically.

## See Also

### Related Documentation
- [Tab View Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TabView/TabView.html#//apple_ref/doc/uid/10000074i)
- [var identifier: Any?](./identifier.md)
  Sets the receiver’s optional identifier object to `identifier`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewitem/init(identifier:))*