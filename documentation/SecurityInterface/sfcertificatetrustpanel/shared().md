# shared()

**Framework**: Security Interface  
**Kind**: method  
**Role**: Type Method

Returns a fully initialized, singleton certificate trust panel object.

**Availability**:
- macOS 10.3+

## Declaration

```swift
class func shared() -> SFCertificateTrustPanel!
```

```objc
+ (SFCertificateTrustPanel *) sharedCertificateTrustPanel;
```

## Discussion

Use this method if your application displays a single certificate trust panel or sheet at a time. If your application can display multiple certificate trust panels or sheets at once, you must allocate separate object instances (using the [`alloc`](../../ObjectiveC/nsobject-swift.class/alloc.md) class method inherited from [`NSObject`](../../ObjectiveC/nsobject-swift.class.md)) and initialize (using the [`init()`](../../ObjectiveC/nsobject-swift.class/init%28%29.md) instance method, also inherited from [`NSObject`](../../ObjectiveC/nsobject-swift.class.md)) instead of using this class method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificatetrustpanel/shared())*