# commitEditing(withDelegate:didCommit:contextInfo:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func commitEditing(withDelegate delegate: Any?, didCommit didCommitSelector: Selector?, contextInfo: UnsafeMutableRawPointer?)
```

```objc
- (void) commitEditingWithDelegate:(id) delegate didCommitSelector:(SEL) didCommitSelector contextInfo:(void *) contextInfo;
```

## See Also

### Instance Methods
- [func commitEditing() -> Bool](./commitediting%28%29.md)
- [func commitEditingWithoutPresentingError() throws](./commiteditingwithoutpresentingerror%28%29.md)
- [func discardEditing()](./discardediting%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nseditor/commitediting(withdelegate:didcommit:contextinfo:))*