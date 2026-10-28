# AMError.Code

**Framework**: Automator  
**Kind**: enum  
**Role**: Enumeration

Automator error codes.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
enum Code
```

```c
enum AMErrorCode : NSInteger;
```

## Overview

These constants are [`NSError`](../../Foundation/nserror.md) code numbers in the Automator error domain ([`AMAutomatorErrorDomain`](../amautomatorerrordomain.md)). You’ll obtain these error codes from the instances of [`NSError`](../../Foundation/nserror.md) returned, for example, by certain methods of [`AMWorkflow`](../amworkflow.md) and [`AMWorkflowController`](../amworkflowcontroller.md). For related information, see [`AMActionErrorKey`](../amactionerrorkey.md).

## Topics

### Workflow Errors
- [AMError.Code.workflowActionsNotLoadedError](./code/workflowactionsnotloadederror.md)
  An error that indicates one of the actions of the workflow couldn’t be loaded.
- [AMError.Code.workflowNewerActionVersionError](./code/workflowneweractionversionerror.md)
  An error that indicates an action in a workflow is newer than the installed action.
- [AMError.Code.workflowNewerVersionError](./code/workflownewerversionerror.md)
  An error that indicates an attempt to open a workflow document that was saved with a newer version of Automator.
- [AMError.Code.workflowNoEnabledActionsError](./code/workflownoenabledactionserror.md)
  An error that indicates there are no enabled actions in the workflow.
- [AMError.Code.workflowOlderActionVersionError](./code/workflowolderactionversionerror.md)
  An error that indicates an action in a workflow is older than the installed action.
- [AMError.Code.workflowPropertyListInvalidError](./code/workflowpropertylistinvaliderror.md)
  An error that indicates an attempt to open a workflow document whose property list couldn’t be read.
### Workflow Runtime Errors
- [AMError.Code.userCanceledError](./code/usercancelederror.md)
  An error that indicates the user cancelled.
### Action Errors
- [AMError.Code.actionApplicationResourceError](./code/actionapplicationresourceerror.md)
  An error that indicates an app required by the action is not found.
- [AMError.Code.actionApplicationVersionResourceError](./code/actionapplicationversionresourceerror.md)
  An error that indicates an app required by the action is the wrong version.
- [AMError.Code.actionArchitectureMismatchError](./code/actionarchitecturemismatcherror.md)
  An error that indicates the action’s binary is not compatible with the current processor.
- [AMError.Code.actionExceptionError](./code/actionexceptionerror.md)
  An error that indicates an action encounters an exception while running.
- [AMError.Code.actionExecutionError](./code/actionexecutionerror.md)
  An error that indicates an action encounters an error while running (reason unknown).
- [AMError.Code.actionFailedGatekeeperError](./code/actionfailedgatekeepererror.md)
  An error that indicates the action doesn’t meet the Gatekeeper security policy.
- [AMError.Code.actionFileResourceError](./code/actionfileresourceerror.md)
  An error that indicates a file required by the action is not found.
- [AMError.Code.actionInitializationError](./code/actioninitializationerror.md)
  An error that indicates Automator is unable to initialize an action (reason unknown).
- [AMError.Code.actionInsufficientDataError](./code/actioninsufficientdataerror.md)
  An error that indicates the action requires input data to run, but none was supplied.
- [AMError.Code.actionIsDeprecatedError](./code/actionisdeprecatederror.md)
  An error that indicates the action has been deprecated.
- [AMError.Code.actionLicenseResourceError](./code/actionlicenseresourceerror.md)
  An error that indicates a license required by the action was not found.
- [AMError.Code.actionLinkError](./code/actionlinkerror.md)
  An error that indicates the action’s executable failed to load due to linking issues.
- [AMError.Code.actionLoadError](./code/actionloaderror.md)
  An error that indicates the action’s executable failed to load.
- [AMError.Code.actionMalwareError](./code/actionmalwareerror.md)
  An error that indicates the action has been identified as malware by XProtect.
- [AMError.Code.actionNotLoadableError](./code/actionnotloadableerror.md)
  An error that indicates the action’s executable is of a type that is not loadable in the current process.
- [AMError.Code.actionPropertyListInvalidError](./code/actionpropertylistinvaliderror.md)
  An error that indicates the property list for an action is invalid.
- [AMError.Code.actionQuarantineError](./code/actionquarantineerror.md)
  An error that indicates action has been quarantined by XProtect, the antimalware system on the Mac.
- [AMError.Code.actionRequiredActionResourceError](./code/actionrequiredactionresourceerror.md)
  An error that indicates an action required by the action is not loaded.
- [AMError.Code.actionRuntimeMismatchError](./code/actionruntimemismatcherror.md)
  An error that indicates an attempt was made to load an action that is not compiled in a way that is compatible with the current app.
- [AMError.Code.actionSignatureCorruptError](./code/actionsignaturecorrupterror.md)
  An error that indicates developer signature for this action is corrupted.
- [AMError.Code.actionThirdPartyActionsNotAllowedError](./code/actionthirdpartyactionsnotallowederror.md)
  An error that indicates the action is a third party action, and loading it has not been allowed by the user.
- [AMError.Code.actionXPCError](./code/actionxpcerror.md)
  An error that indicates the remote process running the action has crashed.
- [AMError.Code.actionXProtectError](./code/actionxprotecterror.md)
  An error that indicates XProtect is unable to successfully analyze the action.
- [AMError.Code.noSuchActionError](./code/nosuchactionerror.md)
  An error that indicates the action could not be located on the system.
### Data Conversion Errors
- [AMError.Code.conversionFailedError](./code/conversionfailederror.md)
  An error that occurs when, for example, the converter encounters an error converting data from one type to another.
- [AMError.Code.conversionNoDataError](./code/conversionnodataerror.md)
  An error that occurs when the converter determines that the conversion, though possible, would produce a nil result.
- [AMError.Code.conversionNotPossibleError](./code/conversionnotpossibleerror.md)
  An error that occurs when the converter determines that it is unable to convert from one data type to another.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Errors
- [var AMAutomatorErrorDomain: String](../amautomatorerrordomain.md)
  A string that identifies the Automator error domain.
- [var AMActionErrorKey: String](../amactionerrorkey.md)
  A key to retrieve the action that caused an error.
- [struct AMError](../amerror.md)
  An Automator error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amerror/code)*