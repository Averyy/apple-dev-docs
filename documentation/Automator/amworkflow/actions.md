# actions

**Framework**: Automator  
**Kind**: property  
**Role**: Instance Property

An array of the workflow’s actions.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
var actions: [AMAction] { get }
```

```objc
@property (nonatomic, strong, readonly) NSArray<__kindof AMAction *> * actions;
```

#### Return Value

An array of actions for the workflow file. Actions are instances of classes such as [`AMBundleAction`](../ambundleaction.md), [`AMAppleScriptAction`](../amapplescriptaction.md), and [`AMShellScriptAction`](../amshellscriptaction.md).

## See Also

### Getting Information About a Workflow
- [var fileURL: URL?](./fileurl.md)
  A URL that specifies the location of the workflow file.
- [func valueForVariable(withName: String) -> Any?](./valueforvariable%28withname%29.md)
  Returns the value of the workflow variable with the specified name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflow/actions)*