# AMAction

**Framework**: Automator  
**Kind**: class

An abstract class that defines the interface and general characteristics of Automator actions.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
class AMAction
```

#### Overview

Automator is an Apple app that allows users to construct and execute workflows consisting of a sequence of discrete modules called actions. An action performs a specific task, such as copying a file or cropping an image, and passes its output to Automator to give to the next action in the workflow. Actions are currently implemented as loadable bundles owned by objects of the [`AMBundleAction`](ambundleaction.md) class, a subclass of [`AMAction`](amaction.md).

The critically important method declared by [`AMAction`](amaction.md) is [`run(withInput:)`](amaction/run(withinput:).md). When Automator executes a workflow, it sends this message to each action object in the workflow (in workflow sequence), in most cases passing in the output of the previous action as input. The action object performs its task in this method and ends by returning an output object for the next action in the workflow.

Subclassing [`AMAction`](amaction.md) is not recommended. For most situations requiring an enhancement to the Automator framework, it is sufficient to subclass [`AMBundleAction`](ambundleaction.md).

## Topics

### Initializing and Encoding
- [init?(definition: [String : Any]?, fromArchive: Bool)](amaction/init(definition:fromarchive:).md)
  Initializes the action with the specified definition.
- [init(contentsOf: URL) throws](amaction/init(contentsof:).md)
  Loads an Automator action from a file URL.
- [func write(to: NSMutableDictionary)](amaction/write(to:).md)
  Examines the parameters and other configuration information specified in the passed dictionary and adds its own information to it if appropriate.
### Controlling the Action
- [func run(withInput: Any?) throws -> Any](amaction/run(withinput:).md)
  Requests the action to perform its task using the specified input.
- [func runAsynchronously(withInput: Any?)](amaction/runasynchronously(withinput:).md)
  Causes Automator to wait for notification that the action has completed execution, which allows the action to perform an asynchronous operation.
- [func finishRunningWithError((any Error)?)](amaction/finishrunningwitherror(_:).md)
  Causes the action to stop running and return an error, which, in turn, causes the workflow to stop.
- [func willFinishRunning()](amaction/willfinishrunning.md)
  Provides an opportunity for an action to perform cleanup operations, such as closing windows and deallocating memory.
- [func stop()](amaction/stop.md)
  Stops the action from running.
- [func reset()](amaction/reset.md)
  Resets the action to its initial state.
### Initializing and Synchronizing the Action User Interface
- [func activated()](amaction/activated.md)
  Allows the action to synchronize its information with settings in another app.
- [func opened()](amaction/opened.md)
  Allows the action to initialize its user interface.
### Performing Logging
- [enum AMLogLevel](amloglevel.md)
  Logging levels that Automator supports.
### Updating Action Parameters
- [func parametersUpdated()](amaction/parametersupdated.md)
  Requests the action to update its user interface from its stored parameters, which have changed.
- [func updateParameters()](amaction/updateparameters.md)
  Requests the action to update its stored set of parameters from the settings in the action’s user interface.
### Getting Action Information
- [var name: String](amaction/name.md)
  The name of the action.
- [var progressValue: CGFloat](amaction/progressvalue.md)
  A float value between 0 and 1, which indicates how far along the action is while processing.
- [var ignoresInput: Bool](amaction/ignoresinput.md)
  A Boolean value that indicates whether the action acts upon its input or the input is ignored.
- [var output: Any?](amaction/output.md)
  The action’s output.
- [var selectedInputType: String?](amaction/selectedinputtype.md)
  The type of input, in UTI format, of the input received by the action.
- [var selectedOutputType: String?](amaction/selectedoutputtype.md)
  The type of output, in UTI format, of the output to be produced by the action.
- [var isStopped: Bool](amaction/isstopped.md)
  A Boolean value that indicates whether the user clicked the stop button on the parent workflow.
### Performing Cleanup Operations
- [func closed()](amaction/closed.md)
  Invoked by Automator when the receiving action is removed from a workflow, allowing it to perform cleanup operations.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [AMBundleAction](ambundleaction.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AMBundleAction](ambundleaction.md)
  An object that represents an Automator action that’s a loadable bundle.
- [class AMShellScriptAction](amshellscriptaction.md)
  An object that represents Automator actions whose runtime behavior is driven by a shell script or by a Perl or Python script.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amaction)*