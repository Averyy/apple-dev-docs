# defaultAction

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The default action to take for flows of network data that don’t match any of the specified rules.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var defaultAction: NEFilterAction { get }
```

```objc
@property (readonly) NEFilterAction defaultAction;
```

## See Also

### Inspecting Filter Settings
- [var rules: [NEFilterRule]](./rules.md)
  An ordered list of rules that define the filter’s operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltersettings/defaultaction)*