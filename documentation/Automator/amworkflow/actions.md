# actions

**Framework**: Automator  
**Kind**: property

An array of the workflow’s actions.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
var actions: [AMAction] { get }
```

#### Return Value

An array of actions for the workflow file. Actions are instances of classes such as [`AMBundleAction`](ambundleaction.md), [`AMAppleScriptAction`](amapplescriptaction.md), and [`AMShellScriptAction`](amshellscriptaction.md).

## See Also

- [var fileURL: URL?](amworkflow/fileurl.md)
  A URL that specifies the location of the workflow file.
- [func valueForVariable(withName: String) -> Any?](amworkflow/valueforvariable(withname:).md)
  Returns the value of the workflow variable with the specified name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflow/actions)*