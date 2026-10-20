# init(name:handler:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a custom action object with the specified name and handler.

**Availability**:
- macOS 10.13+

## Declaration

```swift
init(name: String, handler: (() -> Bool)? = nil)
```

```objc
- (instancetype) initWithName:(NSString *) name handler:(BOOL (^)()) handler;
```

## See Also

### Creating a Custom Action
- [init(name: String, target: any NSObjectProtocol, selector: Selector)](./init%28name,target,selector%29.md)
  Creates a custom action object with the specified name, target, and selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitycustomaction/init(name:handler:))*