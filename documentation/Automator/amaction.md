# AMAction

**Framework**: Automator  
**Kind**: class  
**Role**: Class

An abstract class that defines the interface and general characteristics of Automator actions.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
class AMAction
```

```objc
@interface AMAction : NSObject
```

## Overview

Automator is an Apple app that allows users to construct and execute workflows consisting of a sequence of discrete modules called actions. An action performs a specific task, such as copying a file or cropping an image, and passes its output to Automator to give to the next action in the workflow. Actions are currently implemented as loadable bundles owned by objects of the [`AMBundleAction`](./ambundleaction.md) class, a subclass of [`AMAction`](./amaction.md).

The critically important method declared by [`AMAction`](./amaction.md) is [`run(withInput:)`](./amaction/run%28withinput%29.md). When Automator executes a workflow, it sends this message to each action object in the workflow (in workflow sequence), in most cases passing in the output of the previous action as input. The action object performs its task in this method and ends by returning an output object for the next action in the workflow.

Subclassing [`AMAction`](./amaction.md) is not recommended. For most situations requiring an enhancement to the Automator framework, it is sufficient to subclass [`AMBundleAction`](./ambundleaction.md).

## Topics

### Initializing and Encoding
- [init?(definition: [String : Any]?, fromArchive: Bool)](./amaction/init%28definition,fromarchive%29.md)
  Initializes the action with the specified definition.
- [init(contentsOf: URL) throws](./amaction/init%28contentsof%29.md)
  Loads an Automator action from a file URL.
- [func write(to: NSMutableDictionary)](./amaction/write%28to%29.md)
  Examines the parameters and other configuration information specified in the passed dictionary and adds its own information to it if appropriate.
### Controlling the Action
- [func run(withInput: Any?) throws -> Any](./amaction/run%28withinput%29.md)
  Requests the action to perform its task using the specified input.
- [func runAsynchronously(withInput: Any?)](./amaction/runasynchronously%28withinput%29.md)
  Causes Automator to wait for notification that the action has completed execution, which allows the action to perform an asynchronous operation.
- [func finishRunningWithError((any Error)?)](./amaction/finishrunningwitherror%28_%29.md)
  Causes the action to stop running and return an error, which, in turn, causes the workflow to stop.
- [func willFinishRunning()](./amaction/willfinishrunning%28%29.md)
  Provides an opportunity for an action to perform cleanup operations, such as closing windows and deallocating memory.
- [func stop()](./amaction/stop%28%29.md)
  Stops the action from running.
- [func reset()](./amaction/reset%28%29.md)
  Resets the action to its initial state.
### Initializing and Synchronizing the Action User Interface
- [func activated()](./amaction/activated%28%29.md)
  Allows the action to synchronize its information with settings in another app.
- [func opened()](./amaction/opened%28%29.md)
  Allows the action to initialize its user interface.
### Performing Logging
- [enum AMLogLevel](./amloglevel.md)
  Logging levels that Automator supports.
- [- logMessageWithLevel:format:](./amaction/logmessagewithlevel_format_.md)
  Displays a message in Automator’s log area.
### Updating Action Parameters
- [func parametersUpdated()](./amaction/parametersupdated%28%29.md)
  Requests the action to update its user interface from its stored parameters, which have changed.
- [func updateParameters()](./amaction/updateparameters%28%29.md)
  Requests the action to update its stored set of parameters from the settings in the action’s user interface.
### Getting Action Information
- [var name: String](./amaction/name.md)
  The name of the action.
- [var progressValue: CGFloat](./amaction/progressvalue.md)
  A float value between 0 and 1, which indicates how far along the action is while processing.
- [var ignoresInput: Bool](./amaction/ignoresinput.md)
  A Boolean value that indicates whether the action acts upon its input or the input is ignored.
- [var output: Any?](./amaction/output.md)
  The action’s output.
- [var selectedInputType: String?](./amaction/selectedinputtype.md)
  The type of input, in UTI format, of the input received by the action.
- [var selectedOutputType: String?](./amaction/selectedoutputtype.md)
  The type of output, in UTI format, of the output to be produced by the action.
- [var isStopped: Bool](./amaction/isstopped.md)
  A Boolean value that indicates whether the user clicked the stop button on the parent workflow.
### Performing Cleanup Operations
- [func closed()](./amaction/closed%28%29.md)
  Invoked by Automator when the receiving action is removed from a workflow, allowing it to perform cleanup operations.
### Initializers
- [init(contentsOfURL: URL) throws](./amaction/init%28contentsofurl%29.md)
### Deprecated
- [- runWithInput:fromAction:error:](./amaction/runwithinput_fromaction_error_.md)
  Requests the action to perform its task using the specified input from the specified action.
- [- didFinishRunningWithError:](./amaction/didfinishrunningwitherror_.md)
  Sent by the action to itself when it has finished running asynchronously.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [AMBundleAction](./ambundleaction.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Actions
- [class AMBundleAction](./ambundleaction.md)
  An object that represents an Automator action that’s a loadable bundle.
- [class AMShellScriptAction](./amshellscriptaction.md)
  An object that represents Automator actions whose runtime behavior is driven by a shell script or by a Perl or Python script.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amaction)*