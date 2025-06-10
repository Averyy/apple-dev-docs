# CLSPredicateKeyPath

**Framework**: ClassKit  
**Kind**: struct

The set of possible key paths you use to search for contexts.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct CLSPredicateKeyPath
```

#### Discussion

Use these predicate key paths when constructing a predicate to send to the [`contexts(matching:completion:)`](clsdatastore/contexts(matching:completion:).md) method.

## Topics

### Predicate Key Paths
- [static let dateCreated: CLSPredicateKeyPath](clspredicatekeypath/datecreated.md)
  The date on which the context was created.
- [static let identifier: CLSPredicateKeyPath](clspredicatekeypath/identifier.md)
  The context’s identifier.
- [static let parent: CLSPredicateKeyPath](clspredicatekeypath/parent.md)
  The context’s direct ancestor in the context hierarchy.
- [static let title: CLSPredicateKeyPath](clspredicatekeypath/title.md)
  The human readable name of the context.
- [static let topic: CLSPredicateKeyPath](clspredicatekeypath/topic.md)
  The context’s topic.
- [static let universalLinkURL: CLSPredicateKeyPath](clspredicatekeypath/universallinkurl.md)
  The context’s universal URL link.
### Initializing a Predicate Key Path
- [init(String)](clspredicatekeypath/init(_:).md)
  Initializes a predicate key path.
- [init(rawValue: String)](clspredicatekeypath/init(rawvalue:).md)
  Initializes a predicate key path with the given value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func contexts(matchingIdentifierPath: [String], completion: ([CLSContext], (any Error)?) -> Void)](clsdatastore/contexts(matchingidentifierpath:completion:).md)
  Fetches all the contexts along a given identifier path.
- [func contexts(matching: NSPredicate, completion: ([CLSContext], (any Error)?) -> Void)](clsdatastore/contexts(matching:completion:).md)
  Fetches all the contexts matching a predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clspredicatekeypath)*