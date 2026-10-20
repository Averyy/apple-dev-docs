# extend(in:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Extends text selection in the specified directions, such as in response to an arrow key press while shift is held.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func extend(in direction: UITextLayoutDirection)
```

```objc
- (void) extendInLayoutDirection:(UITextLayoutDirection) direction;
```

## See Also

### Extending the text section
- [func extend(in: UITextStorageDirection, by: UITextGranularity)](./extend%28in,by%29.md)
  Moves the selection in the specified directions by granularity, in response to different key combinations:


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextselectiondirectionnavigation/extend(in:))*