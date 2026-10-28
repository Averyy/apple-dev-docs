# valid

**Framework**: BrowserEngineKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the system grants the capability.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```objc
@property (readonly, getter=isValid) BOOL valid;
```

## Discussion

The system sets this property to `true` if the system grants the capability; otherwise, the value is `false`.

## See Also

### Testing and changing validity
- [- invalidate](./invalidate.md)
  Revokes access to a capability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beprocesscapabilitygrant/valid)*