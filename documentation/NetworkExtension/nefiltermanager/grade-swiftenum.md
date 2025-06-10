# NEFilterManager.Grade

**Framework**: Network Extension  
**Kind**: enum

A type for the grade or priority of the filter.

**Availability**:
- macOS 10.15+

## Declaration

```swift
enum Grade
```

## Topics

### Grades
- [NEFilterManager.Grade.firewall](nefiltermanager/grade-swift.enum/firewall.md)
  A grade for filters that act as firewalls, blocking some network traffic.
- [NEFilterManager.Grade.inspector](nefiltermanager/grade-swift.enum/inspector.md)
  A grade for filters that act as inspectors of network traffic.
### Initializers
- [init?(rawValue: Int)](nefiltermanager/grade-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var grade: NEFilterManager.Grade](nefiltermanager/grade-swift.property.md)
  The grade of the filter, which determines when it acts relative to other filters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltermanager/grade-swift.enum)*