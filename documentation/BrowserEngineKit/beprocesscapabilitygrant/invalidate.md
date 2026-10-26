# invalidate

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Revokes access to a capability.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```objc
- (BOOL) invalidate;
```

#### Discussion

This method invalidates a grant and removes the capability from the process.

## See Also

### Testing and changing validity
- [valid](./valid.md)
  A Boolean value that indicates whether the system grants the capability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beprocesscapabilitygrant/invalidate)*