# ContentState

**Framework**: ActivityKit  
**Kind**: associatedtype  
**Required**: Yes

The associated type that describes the dynamic content of a Live Activity.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
associatedtype ContentState : Decodable, Encodable, Hashable
```

#### Discussion

The dynamic data of a Live Activity that’s encoded by `ContentState` can’t exceed 4KB.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activityattributes/contentstate)*