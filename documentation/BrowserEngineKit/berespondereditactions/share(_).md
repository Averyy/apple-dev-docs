# share(_:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Presents UI for sharing the selected text.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
optional func share(_ sender: Any?)
```

```objc
- (void) share:(id) sender;
```

## Discussion

To present the standard system UI for sharing content, call [`share(text:from:)`](../betextinteraction/share%28text,from%29.md) in your implementation of this method.

## Parameters

- `sender`: The object calling this method.

## See Also

### Defining and sharing text
- [func lookup(Any?)](./lookup%28_%29.md)
  Presents a dictionary definition for the selected content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/berespondereditactions/share(_:))*