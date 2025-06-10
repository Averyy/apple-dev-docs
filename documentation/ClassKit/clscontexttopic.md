# CLSContextTopic

**Framework**: ClassKit  
**Kind**: struct

The areas of study to which contexts may relate.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct CLSContextTopic
```

## Mentions

- [Building missing contexts](building-missing-contexts.md)

#### Discussion

After you initialize a context, you can assign it a topic by setting its [`topic`](clscontext/topic.md) property. Doing so helps teachers browsing your app’s content to understand what your app offers.

## Topics

### Context Topics
- [static let artsAndMusic: CLSContextTopic](clscontexttopic/artsandmusic.md)
  Arts and music.
- [static let computerScienceAndEngineering: CLSContextTopic](clscontexttopic/computerscienceandengineering.md)
  Computer science and engineering.
- [static let healthAndFitness: CLSContextTopic](clscontexttopic/healthandfitness.md)
  Health and fitness.
- [static let literacyAndWriting: CLSContextTopic](clscontexttopic/literacyandwriting.md)
  Literacy and writing.
- [static let math: CLSContextTopic](clscontexttopic/math.md)
  Mathematics.
- [static let science: CLSContextTopic](clscontexttopic/science.md)
  Science.
- [static let socialScience: CLSContextTopic](clscontexttopic/socialscience.md)
  Social science.
- [static let worldLanguage: CLSContextTopic](clscontexttopic/worldlanguage.md)
  Language acquisition.
### Initializing a Topic
- [init(rawValue: String)](clscontexttopic/init(rawvalue:).md)
  Initializes a context topic.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var displayOrder: Int](clscontext/displayorder.md)
  The position of a context relative to its siblings.
- [var topic: CLSContextTopic?](clscontext/topic.md)
  The area of study to which a context relates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clscontexttopic)*