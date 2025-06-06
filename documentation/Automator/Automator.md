# Automator

**Framework**: Automator  
**Kind**: module

Develop actions that the Automator app can load and run. View, edit, and run Automator workflows in your app.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

#### Overview

The Automator framework supports the development of actions for the Automator app, as well as the ability to run a workflow in developer apps. An  is a bundle that, when loaded and run, performs a specific task, such as copying a file or cropping an image. Using Automator, users can construct and execute  consisting of a sequence of actions. Developers can also load and execute workflows in their apps. As a workflow executes, the output of one action is typically passed as the input to the next action. Automator loads action bundles from standard locations in the file system: `/System/Library/Automator`, `/Library/Automator`, and `~/Library/Automator`.

## Topics

### Actions
- [class AMBundleAction](ambundleaction.md)
  An object that represents an Automator action that’s a loadable bundle.
- [class AMShellScriptAction](amshellscriptaction.md)
  An object that represents Automator actions whose runtime behavior is driven by a shell script or by a Perl or Python script.
- [class AMAction](amaction.md)
  An abstract class that defines the interface and general characteristics of Automator actions.
### Workflows
- [class AMWorkflow](amworkflow.md)
  An object that lets you use an Automator workflow in your app.
- [class AMWorkflowController](amworkflowcontroller.md)
  An object that lets you manage an Automator workflow in your app.
- [class AMWorkflowView](amworkflowview.md)
  An object that lets you view and edit Automator workflows in your app.
- [class AMWorkspace](amworkspace.md)
  A workspace for running an Automator workflow.
### Errors
- [var AMAutomatorErrorDomain: String](amautomatorerrordomain.md)
  A string that identifies the Automator error domain.
- [var AMActionErrorKey: String](amactionerrorkey.md)
  A key to retrieve the action that caused an error.
- [struct AMError](amerror.md)
  An Automator error.
- [AMError.Code](amerror/code.md)
  Automator error codes.
### Deprecated
- [class AMAppleScriptAction](amapplescriptaction.md)
  An object that represents Automator actions whose runtime behavior is driven by an AppleScript script.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Automator)*