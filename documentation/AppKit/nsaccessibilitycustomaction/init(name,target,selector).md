# init(name:target:selector:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a custom action object with the specified name, target, and selector.

**Availability**:
- macOS 10.13+

## Declaration

```swift
init(name: String, target: any NSObjectProtocol, selector: Selector)
```

```objc
- (instancetype) initWithName:(NSString *) name target:(id<NSObject>) target selector:(SEL) selector;
```

## See Also

### Creating a Custom Action
- [init(name: String, handler: (() -> Bool)?)](./init%28name,handler%29.md)
  Creates a custom action object with the specified name and handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitycustomaction/init(name:target:selector:))*