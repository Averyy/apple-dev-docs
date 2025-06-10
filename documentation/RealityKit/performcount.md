# performCount

**Framework**: RealityKit

A value that specifies the number of times the group’s actions repeat.

#### Overview

The default value is `1`, which execute the actions only once. If the value is `0` and `loops` is set to `true`, the actions execute infinitely. If the value is a number () and the type is `serial`, the actions execute  times in sequence. And if the value is set to a number () and the type is `parallel`, the actions execute  times independently.

##### Declaration

```other
uniform uint performCount = 1
```

## See Also

- [info:id](info-id.md)
  The action’s unique identifier.
- [type](type.md)
  An option that controls the order in which the actions execute.
- [loops](loops.md)
  A Boolean value indicating whether the group loops.
- [actions](actions.md)
  A list of actions that make up the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/performcount)*