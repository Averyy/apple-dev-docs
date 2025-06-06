# connect(to:completionHandler:)

**Framework**: Core NFC  
**Kind**: method

Connects the reader session to a tag and activates that tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func connect(to tag: any NFCNDEFTag) async throws
```

#### Discussion

A tag stays connected until your app connects to a different tag or restarts polling. Connecting to a tag that is already connected has no effect.

## Parameters

- `tag`: A tag that the reader session should attempt connecting to.
- `completionHandler`: The session calls   on the dispatch queue provided when creating the  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndefreadersession/connect(to:completionhandler:))*