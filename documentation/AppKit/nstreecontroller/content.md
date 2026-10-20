# content

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The tree controller’s content object.

**Availability**:
- macOS

## Declaration

```swift
var content: Any? { get set }
```

```objc
@property (strong, nullable) id content;
```

#### Discussion

The value of this property can be an array of objects, or a single root object. The default value is `nil`. This property is observable using key-value observing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreecontroller/content)*