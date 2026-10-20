# grade

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The grade of the filter, which determines when it acts relative to other filters.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var grade: NEFilterManager.Grade { get set }
```

```objc
@property NEFilterManagerGrade grade;
```

#### Discussion

The default grade is [`NEFilterManager.Grade.firewall`](./grade-swift.enum/firewall.md).

## See Also

### Prioritizing filters
- [NEFilterManager.Grade](./grade-swift.enum.md)
  A type for the grade or priority of the filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltermanager/grade-swift.property)*