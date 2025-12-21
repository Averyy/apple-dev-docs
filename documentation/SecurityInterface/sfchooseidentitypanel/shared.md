# shared()

**Framework**: Security Interface  
**Kind**: method

Returns a fully initialized, singleton choose identity panel object.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
class func shared() -> SFChooseIdentityPanel!
```

#### Discussion

Use this method if your application displays a single choose identity panel or sheet at a time. If your application can display multiple choose identity panels or sheets at once, you must allocate separate object instances (using the [`alloc`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/alloc) class method inherited from [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)) and initialize them (using the [`init()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/init()) instance method, also inherited from [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)) instead of using this class method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfchooseidentitypanel/shared())*