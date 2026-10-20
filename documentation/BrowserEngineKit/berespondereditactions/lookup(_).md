# lookup(_:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Presents a dictionary definition for the selected content.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
optional func lookup(_ sender: Any?)
```

```objc
- (void) lookup:(id) sender;
```

#### Discussion

To present the standard system UI for showing a dictionary definition, call [`showDictionary(forTextInContext:definingTextInRange:from:)`](../betextinteraction/showdictionary%28fortextincontext,definingtextinrange,from%29.md) in your implementation of this method.

## Parameters

- `sender`: The object calling this method.

## See Also

### Defining and sharing text
- [func share(Any?)](./share%28_%29.md)
  Presents UI for sharing the selected text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/berespondereditactions/lookup(_:))*