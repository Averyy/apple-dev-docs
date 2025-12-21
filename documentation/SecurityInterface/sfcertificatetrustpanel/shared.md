# shared()

**Framework**: Security Interface  
**Kind**: method

Returns a fully initialized, singleton certificate trust panel object.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
class func shared() -> SFCertificateTrustPanel!
```

#### Discussion

Use this method if your application displays a single certificate trust panel or sheet at a time. If your application can display multiple certificate trust panels or sheets at once, you must allocate separate object instances (using the [`alloc`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/alloc) class method inherited from [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)) and initialize (using the [`init()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/init()) instance method, also inherited from [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)) instead of using this class method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificatetrustpanel/shared())*