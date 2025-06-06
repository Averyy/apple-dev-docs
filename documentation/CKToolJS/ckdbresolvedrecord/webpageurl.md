# webpageUrl

**Framework**: CKTool JS  
**Kind**: property

The fallback URL that you can redirect users to if the operation fails.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
attribute string? webpageUrl;
```

#### Discussion

An operation might fail, if a resolve/accept endpoint doesn’t succeed. If that happens, this value would be the URL that you could redirect users to. You can set the fallback URL using CloudKit Dashboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/ckdbresolvedrecord/webpageurl)*