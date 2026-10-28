# fileURL

**Framework**: Automator  
**Kind**: property  
**Role**: Instance Property

A URL that specifies the location of the workflow file.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
var fileURL: URL? { get }
```

```objc
@property (copy, readonly, nullable) NSURL * fileURL;
```

## Return Value

URL that specifies the location of the workflow file.

## See Also

### Getting Information About a Workflow
- [var actions: [AMAction]](./actions.md)
  An array of the workflow’s actions.
- [func valueForVariable(withName: String) -> Any?](./valueforvariable%28withname%29.md)
  Returns the value of the workflow variable with the specified name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflow/fileurl)*