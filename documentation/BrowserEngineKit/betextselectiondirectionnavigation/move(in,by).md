# move(in:by:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Moves the cursor in the specified directions by granularity, in response to different key combinations:

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func move(in direction: UITextStorageDirection, by granularity: UITextGranularity)
```

```objc
- (void) moveInStorageDirection:(UITextStorageDirection) direction byGranularity:(UITextGranularity) granularity;
```

## Discussion

Option + left/right = word Option + up/down = paragraph Command + left/right = line Command + up/down = document

## See Also

### Moving the cursor
- [func move(in: UITextLayoutDirection)](./move%28in%29.md)
  Moves the cursor in the specified directions, such as in response to an arrow key press.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextselectiondirectionnavigation/move(in:by:))*