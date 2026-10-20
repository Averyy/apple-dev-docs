# identifier

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The unique identifier of the context object.

**Availability**:
- macOS 15.2+

## Declaration

```swift
var identifier: UUID { get }
```

```objc
@property (strong, readonly) NSUUID * identifier;
```

#### Discussion

The [`NSWritingToolsCoordinator.Context`](../context.md) object initializes the value of this property at creation time. Use this value to identify the context object within your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/context/identifier)*