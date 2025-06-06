# AMError

**Framework**: Automator  
**Kind**: struct

An Automator error.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
struct AMError
```

## Topics

### Error Codes
- [static var workflowActionsNotLoadedError: AMError.Code](amerror/workflowactionsnotloadederror.md)
  An error that indicates one of the actions of the workflow couldn’t be loaded.
- [static var workflowNewerActionVersionError: AMError.Code](amerror/workflowneweractionversionerror.md)
  An error that indicates an action in a workflow is newer than the installed action.
- [static var workflowNewerVersionError: AMError.Code](amerror/workflownewerversionerror.md)
  An error that indicates an attempt to open a workflow document that was saved with a newer version of Automator.
- [static var workflowNoEnabledActionsError: AMError.Code](amerror/workflownoenabledactionserror.md)
  An error that indicates there are no enabled actions in the workflow.
- [static var workflowOlderActionVersionError: AMError.Code](amerror/workflowolderactionversionerror.md)
  An error that indicates an action in a workflow is older than the installed action.
- [static var workflowPropertyListInvalidError: AMError.Code](amerror/workflowpropertylistinvaliderror.md)
  An error that indicates an attempt to open a workflow document whose property list couldn’t be read.
- [static var userCanceledError: AMError.Code](amerror/usercancelederror.md)
  An error that indicates the user cancelled.
- [static var actionApplicationResourceError: AMError.Code](amerror/actionapplicationresourceerror.md)
  An error that indicates an app required by the action is not found.
- [static var actionApplicationVersionResourceError: AMError.Code](amerror/actionapplicationversionresourceerror.md)
  An error that indicates an app required by the action is the wrong version.
- [static var actionArchitectureMismatchError: AMError.Code](amerror/actionarchitecturemismatcherror.md)
  An error that indicates the action’s binary is not compatible with the current processor.
- [static var actionExceptionError: AMError.Code](amerror/actionexceptionerror.md)
  An error that indicates an action encounters an exception while running.
- [static var actionExecutionError: AMError.Code](amerror/actionexecutionerror.md)
  An error that indicates an action encounters an error while running (reason unknown).
- [static var actionFailedGatekeeperError: AMError.Code](amerror/actionfailedgatekeepererror.md)
  An error that indicates the action doesn’t meet the Gatekeeper security policy.
- [static var actionFileResourceError: AMError.Code](amerror/actionfileresourceerror.md)
  An error that indicates a file required by the action is not found.
- [static var actionInitializationError: AMError.Code](amerror/actioninitializationerror.md)
  An error that indicates Automator is unable to initialize an action (reason unknown).
- [static var actionInsufficientDataError: AMError.Code](amerror/actioninsufficientdataerror.md)
  An error that indicates the action requires input data to run, but none was supplied.
- [static var actionIsDeprecatedError: AMError.Code](amerror/actionisdeprecatederror.md)
  An error that indicates the action has been deprecated.
- [static var actionLicenseResourceError: AMError.Code](amerror/actionlicenseresourceerror.md)
  An error that indicates a license required by the action was not found.
- [static var actionLinkError: AMError.Code](amerror/actionlinkerror.md)
  An error that indicates the action’s executable failed to load due to linking issues.
- [static var actionLoadError: AMError.Code](amerror/actionloaderror.md)
  An error that indicates the action’s executable failed to load.
- [static var actionMalwareError: AMError.Code](amerror/actionmalwareerror.md)
  An error that indicates the action has been identified as malware by XProtect.
- [static var actionNotLoadableError: AMError.Code](amerror/actionnotloadableerror.md)
  An error that indicates the action’s executable is of a type that is not loadable in the current process.
- [static var actionPropertyListInvalidError: AMError.Code](amerror/actionpropertylistinvaliderror.md)
  An error that indicates the property list for an action is invalid.
- [static var actionQuarantineError: AMError.Code](amerror/actionquarantineerror.md)
  An error that indicates action has been quarantined by XProtect, the antimalware system on the Mac.
- [static var actionRequiredActionResourceError: AMError.Code](amerror/actionrequiredactionresourceerror.md)
  An error that indicates an action required by the action is not loaded.
- [static var actionRuntimeMismatchError: AMError.Code](amerror/actionruntimemismatcherror.md)
  An error that indicates an attempt was made to load an action that is not compiled in a way that is compatible with the current app.
- [static var actionSignatureCorruptError: AMError.Code](amerror/actionsignaturecorrupterror.md)
  An error that indicates developer signature for this action is corrupted.
- [static var actionThirdPartyActionsNotAllowedError: AMError.Code](amerror/actionthirdpartyactionsnotallowederror.md)
  An error that indicates the action is a third party action, and loading it has not been allowed by the user.
- [static var actionXPCError: AMError.Code](amerror/actionxpcerror.md)
  An error that indicates the remote process running the action has crashed.
- [static var actionXProtectError: AMError.Code](amerror/actionxprotecterror.md)
  An error that indicates XProtect is unable to successfully analyze the action.
- [static var noSuchActionError: AMError.Code](amerror/nosuchactionerror.md)
  An error that indicates the action could not be located on the system.
- [static var conversionFailedError: AMError.Code](amerror/conversionfailederror.md)
  An error that occurs when, for example, the converter encounters an error converting data from one type to another.
- [static var conversionNoDataError: AMError.Code](amerror/conversionnodataerror.md)
  An error that occurs when the converter determines that the conversion, though possible, would produce a nil result.
- [static var conversionNotPossibleError: AMError.Code](amerror/conversionnotpossibleerror.md)
  An error that occurs when the converter determines that it is unable to convert from one data type to another.
- [AMError.Code](amerror/code.md)
  Automator error codes.
### Error Domain
- [var AMAutomatorErrorDomain: String](amautomatorerrordomain.md)
  A string that identifies the Automator error domain.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var AMAutomatorErrorDomain: String](amautomatorerrordomain.md)
  A string that identifies the Automator error domain.
- [var AMActionErrorKey: String](amactionerrorkey.md)
  A key to retrieve the action that caused an error.
- [AMError.Code](amerror/code.md)
  Automator error codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amerror)*