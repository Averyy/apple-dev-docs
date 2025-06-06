# userCanceledError

**Framework**: Automator  
**Kind**: property

An error that indicates the user cancelled.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
static var userCanceledError: AMError.Code { get }
```

#### Discussion

This error is the same as the AppleScript error [`userCanceledErr`](https://developer.apple.com/documentation/kernel/1645157-anonymous/usercancelederr). When an Apple Event is canceled by the user, a running action may return this error. Automator ignores the error and stops the workflow gracefully, without displaying the error to the user.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amerror/usercancelederror)*