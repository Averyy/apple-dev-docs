# NEFilterManager.Grade

**Framework**: Network Extension  
**Kind**: enum  
**Role**: Enumeration

A type for the grade or priority of the filter.

**Availability**:
- macOS 10.15+

## Declaration

```swift
enum Grade
```

```c
enum NEFilterManagerGrade : NSInteger;
```

## Topics

### Grades
- [NEFilterManager.Grade.firewall](./grade-swift.enum/firewall.md)
  A grade for filters that act as firewalls, blocking some network traffic.
- [NEFilterManager.Grade.inspector](./grade-swift.enum/inspector.md)
  A grade for filters that act as inspectors of network traffic.
### Initializers
- [init?(rawValue: Int)](./grade-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Prioritizing filters
- [var grade: NEFilterManager.Grade](./grade-swift.property.md)
  The grade of the filter, which determines when it acts relative to other filters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltermanager/grade-swift.enum)*