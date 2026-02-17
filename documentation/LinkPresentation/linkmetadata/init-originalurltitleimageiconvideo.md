# init(originalURL:title:image:icon:video:)

**Framework**: Link Presentation  
**Kind**: init

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)
- tvOS 26.4+ (Beta)
- visionOS 26.4+ (Beta)
- watchOS 26.4+ (Beta)

## Declaration

```swift
nonisolated
init<A, B, C>(originalURL: URL?, title: String? = nil, image: A? = Never?.none, icon: B? = Never?.none, video: C? = Never?.none) where A : Transferable, B : Transferable, C : Transferable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/linkpresentation/linkmetadata/init(originalurl:title:image:icon:video:))*