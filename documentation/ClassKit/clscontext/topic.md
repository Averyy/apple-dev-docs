# topic

**Framework**: ClassKit  
**Kind**: property

The area of study to which a context relates.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var topic: CLSContextTopic? { get set }
```

#### Discussion

Set the topic to tell teachers what kind of content a given context covers using one of the values from [`CLSContextTopic`](clscontexttopic.md). The topic set on a context applies to that context and any of its descendants for which you haven’t explicitly set a topic. So if your entire app covers only a single topic, you only need to set the topic for the [`mainAppContext`](clsdatastore/mainappcontext.md).

## See Also

- [var displayOrder: Int](clscontext/displayorder.md)
  The position of a context relative to its siblings.
- [struct CLSContextTopic](clscontexttopic.md)
  The areas of study to which contexts may relate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clscontext/topic)*