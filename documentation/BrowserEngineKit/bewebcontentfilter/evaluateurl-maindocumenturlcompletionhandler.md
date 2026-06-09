# evaluateURL(_:mainDocumentURL:completionHandler:)

**Framework**: BrowserEngineKit  
**Kind**: method

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
func evaluateURL(_ url: URL, mainDocumentURL: URL?) async -> (Bool, Data?)
```

#### Discussion

Evaluates whether a URL should be blocked and if yes, provides a response body representing the HTML of the blocking content that will be displayed in either the blocked main document or blocked subframe.

## Parameters

- `url`: The URL to be evaluated.
- `mainDocumentURL`: The URL of the main document, also the root URL of the transitive trust policy
- `completionHandler`: The completion block to be invoked when evaluation is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bewebcontentfilter/evaluateurl(_:maindocumenturl:completionhandler:))*