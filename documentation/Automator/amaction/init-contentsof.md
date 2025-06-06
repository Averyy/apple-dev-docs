# init(contentsOf:)

**Framework**: Automator  
**Kind**: init

Loads an Automator action from a file URL.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.5+

## Declaration

```swift
init(contentsOf fileURL: URL) throws
```

#### Return Value

The initialized action.

#### Discussion

This method is typically invoked by app that use the [`AMWorkflow`](amworkflow.md) class to embed Automator workflows. It is used to allow creation of actions for a workflow.

## Parameters

- `fileURL`: URL that specifies the location of an action file.

## See Also

- [init?(definition: [String : Any]?, fromArchive: Bool)](amaction/init(definition:fromarchive:).md)
  Initializes the action with the specified definition.
- [func write(to: NSMutableDictionary)](amaction/write(to:).md)
  Examines the parameters and other configuration information specified in the passed dictionary and adds its own information to it if appropriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amaction/init(contentsof:))*