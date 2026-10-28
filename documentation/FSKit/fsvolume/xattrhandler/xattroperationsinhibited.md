# xattrOperationsInhibited

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that instructs FSKit not to call this protocol’s methods, even if the volume conforms to it.

**Availability**:
- macOS 27.0+

## Declaration

```swift
optional var xattrOperationsInhibited: Bool { get }
```

```objc
@property (readonly) BOOL xattrOperationsInhibited;
```

## Discussion

FSKit reads this value after the file system replies to the `loadResource` message. Changing the returned value during the runtime of the volume has no effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/xattrhandler/xattroperationsinhibited)*