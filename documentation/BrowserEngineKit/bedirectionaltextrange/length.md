# length

**Framework**: BrowserEngineKit  
**Kind**: property  
**Role**: Instance Property

The number of characters included in the directional text range.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var length: Int
```

```c
NSInteger length;
```

#### Discussion

The sign of this value indicates a direction for the text selection:

- Positive length indicates forward selection.
- Negative length indicates backward selection.

## See Also

### Measuring text range
- [var offset: Int](./offset.md)
  The starting position of the directional text range within the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bedirectionaltextrange/length)*