# init(contentsOf:)

**Framework**: Automator  
**Kind**: init  
**Role**: Initializer

Loads an Automator action from a file URL.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.5+

## Declaration

```swift
init(contentsOf fileURL: URL) throws
```

```objc
- (instancetype) initWithContentsOfURL:(NSURL *) fileURL error:(NSError **) outError;
```

## Return Value

The initialized action.

## Discussion

This method is typically invoked by app that use the [`AMWorkflow`](../amworkflow.md) class to embed Automator workflows. It is used to allow creation of actions for a workflow.

## Parameters

- `fileURL`: URL that specifies the location of an action file.

## See Also

### Initializing and Encoding
- [init?(definition: [String : Any]?, fromArchive: Bool)](./init%28definition,fromarchive%29.md)
  Initializes the action with the specified definition.
- [func write(to: NSMutableDictionary)](./write%28to%29.md)
  Examines the parameters and other configuration information specified in the passed dictionary and adds its own information to it if appropriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amaction/init(contentsof:))*