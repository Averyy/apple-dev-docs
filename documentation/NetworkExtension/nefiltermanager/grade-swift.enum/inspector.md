# NEFilterManager.Grade.inspector

**Framework**: Network Extension  
**Kind**: case  
**Role**: Case

A grade for filters that act as inspectors of network traffic.

**Availability**:
- macOS 10.15+

## Declaration

```swift
case inspector
```

```c
NEFilterManagerGradeInspector
```

#### Discussion

Inspector grade filters see network traffic after firewall grade filters.

## See Also

### Grades
- [NEFilterManager.Grade.firewall](./firewall.md)
  A grade for filters that act as firewalls, blocking some network traffic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltermanager/grade-swift.enum/inspector)*