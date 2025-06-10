# AMError.Code

**Framework**: Automator  
**Kind**: enum

Automator error codes.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
enum Code
```

#### Overview

These constants are [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) code numbers in the Automator error domain ([`AMAutomatorErrorDomain`](amautomatorerrordomain.md)). You’ll obtain these error codes from the instances of [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) returned, for example, by certain methods of [`AMWorkflow`](amworkflow.md) and [`AMWorkflowController`](amworkflowcontroller.md). For related information, see [`AMActionErrorKey`](amactionerrorkey.md).

## Topics

### Workflow Errors
- [AMError.Code.workflowActionsNotLoadedError](amerror/code/workflowactionsnotloadederror.md)
  An error that indicates one of the actions of the workflow couldn’t be loaded.
- [AMError.Code.workflowNewerActionVersionError](amerror/code/workflowneweractionversionerror.md)
  An error that indicates an action in a workflow is newer than the installed action.
- [AMError.Code.workflowNewerVersionError](amerror/code/workflownewerversionerror.md)
  An error that indicates an attempt to open a workflow document that was saved with a newer version of Automator.
- [AMError.Code.workflowNoEnabledActionsError](amerror/code/workflownoenabledactionserror.md)
  An error that indicates there are no enabled actions in the workflow.
- [AMError.Code.workflowOlderActionVersionError](amerror/code/workflowolderactionversionerror.md)
  An error that indicates an action in a workflow is older than the installed action.
- [AMError.Code.workflowPropertyListInvalidError](amerror/code/workflowpropertylistinvaliderror.md)
  An error that indicates an attempt to open a workflow document whose property list couldn’t be read.
### Workflow Runtime Errors
- [AMError.Code.userCanceledError](amerror/code/usercancelederror.md)
  An error that indicates the user cancelled.
### Action Errors
- [AMError.Code.actionApplicationResourceError](amerror/code/actionapplicationresourceerror.md)
  An error that indicates an app required by the action is not found.
- [AMError.Code.actionApplicationVersionResourceError](amerror/code/actionapplicationversionresourceerror.md)
  An error that indicates an app required by the action is the wrong version.
- [AMError.Code.actionArchitectureMismatchError](amerror/code/actionarchitecturemismatcherror.md)
  An error that indicates the action’s binary is not compatible with the current processor.
- [AMError.Code.actionExceptionError](amerror/code/actionexceptionerror.md)
  An error that indicates an action encounters an exception while running.
- [AMError.Code.actionExecutionError](amerror/code/actionexecutionerror.md)
  An error that indicates an action encounters an error while running (reason unknown).
- [AMError.Code.actionFailedGatekeeperError](amerror/code/actionfailedgatekeepererror.md)
  An error that indicates the action doesn’t meet the Gatekeeper security policy.
- [AMError.Code.actionFileResourceError](amerror/code/actionfileresourceerror.md)
  An error that indicates a file required by the action is not found.
- [AMError.Code.actionInitializationError](amerror/code/actioninitializationerror.md)
  An error that indicates Automator is unable to initialize an action (reason unknown).
- [AMError.Code.actionInsufficientDataError](amerror/code/actioninsufficientdataerror.md)
  An error that indicates the action requires input data to run, but none was supplied.
- [AMError.Code.actionIsDeprecatedError](amerror/code/actionisdeprecatederror.md)
  An error that indicates the action has been deprecated.
- [AMError.Code.actionLicenseResourceError](amerror/code/actionlicenseresourceerror.md)
  An error that indicates a license required by the action was not found.
- [AMError.Code.actionLinkError](amerror/code/actionlinkerror.md)
  An error that indicates the action’s executable failed to load due to linking issues.
- [AMError.Code.actionLoadError](amerror/code/actionloaderror.md)
  An error that indicates the action’s executable failed to load.
- [AMError.Code.actionMalwareError](amerror/code/actionmalwareerror.md)
  An error that indicates the action has been identified as malware by XProtect.
- [AMError.Code.actionNotLoadableError](amerror/code/actionnotloadableerror.md)
  An error that indicates the action’s executable is of a type that is not loadable in the current process.
- [AMError.Code.actionPropertyListInvalidError](amerror/code/actionpropertylistinvaliderror.md)
  An error that indicates the property list for an action is invalid.
- [AMError.Code.actionQuarantineError](amerror/code/actionquarantineerror.md)
  An error that indicates action has been quarantined by XProtect, the antimalware system on the Mac.
- [AMError.Code.actionRequiredActionResourceError](amerror/code/actionrequiredactionresourceerror.md)
  An error that indicates an action required by the action is not loaded.
- [AMError.Code.actionRuntimeMismatchError](amerror/code/actionruntimemismatcherror.md)
  An error that indicates an attempt was made to load an action that is not compiled in a way that is compatible with the current app.
- [AMError.Code.actionSignatureCorruptError](amerror/code/actionsignaturecorrupterror.md)
  An error that indicates developer signature for this action is corrupted.
- [AMError.Code.actionThirdPartyActionsNotAllowedError](amerror/code/actionthirdpartyactionsnotallowederror.md)
  An error that indicates the action is a third party action, and loading it has not been allowed by the user.
- [AMError.Code.actionXPCError](amerror/code/actionxpcerror.md)
  An error that indicates the remote process running the action has crashed.
- [AMError.Code.actionXProtectError](amerror/code/actionxprotecterror.md)
  An error that indicates XProtect is unable to successfully analyze the action.
- [AMError.Code.noSuchActionError](amerror/code/nosuchactionerror.md)
  An error that indicates the action could not be located on the system.
### Data Conversion Errors
- [AMError.Code.conversionFailedError](amerror/code/conversionfailederror.md)
  An error that occurs when, for example, the converter encounters an error converting data from one type to another.
- [AMError.Code.conversionNoDataError](amerror/code/conversionnodataerror.md)
  An error that occurs when the converter determines that the conversion, though possible, would produce a nil result.
- [AMError.Code.conversionNotPossibleError](amerror/code/conversionnotpossibleerror.md)
  An error that occurs when the converter determines that it is unable to convert from one data type to another.
### Initializers
- [init?(rawValue: Int)](amerror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var AMAutomatorErrorDomain: String](amautomatorerrordomain.md)
  A string that identifies the Automator error domain.
- [var AMActionErrorKey: String](amactionerrorkey.md)
  A key to retrieve the action that caused an error.
- [struct AMError](amerror.md)
  An Automator error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amerror/code)*