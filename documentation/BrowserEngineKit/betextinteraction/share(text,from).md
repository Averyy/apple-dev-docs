# share(text:from:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Presents standard UI for someone to share text from a browser text view.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func share(text: String, from presentationRect: CGRect)
```

```objc
- (void) shareText:(NSString *) text fromRect:(CGRect) presentationRect;
```

## Parameters

- `text`: The text to share.
- `presentationRect`: The area in the view containing the text, which the system uses to locate the sharing UI.

## See Also

### Sharing and defining text
- [func showDictionary(forTextInContext: String, definingTextInRange: NSRange, from: CGRect)](./showdictionary%28fortextincontext,definingtextinrange,from%29.md)
  Presents a dictionary definition for the supplied text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinteraction/share(text:from:))*