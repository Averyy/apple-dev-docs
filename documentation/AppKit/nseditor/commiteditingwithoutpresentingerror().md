# commitEditingWithoutPresentingError()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func commitEditingWithoutPresentingError() throws
```

```objc
- (BOOL) commitEditingAndReturnError:(NSError **) error;
```

## See Also

### Instance Methods
- [func commitEditing() -> Bool](./commitediting%28%29.md)
- [func commitEditing(withDelegate: Any?, didCommit: Selector?, contextInfo: UnsafeMutableRawPointer?)](./commitediting%28withdelegate,didcommit,contextinfo%29.md)
- [func discardEditing()](./discardediting%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nseditor/commiteditingwithoutpresentingerror())*