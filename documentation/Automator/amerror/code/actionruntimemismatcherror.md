# AMError.Code.actionRuntimeMismatchError

**Framework**: Automator  
**Kind**: case  
**Role**: Case

An error that indicates an attempt was made to load an action that is not compiled in a way that is compatible with the current app.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
case actionRuntimeMismatchError
```

```c
AMActionRuntimeMismatchError
```

## Discussion

For example, the action may be compiled for 32-bit apps.

## See Also

### Action Errors
- [AMError.Code.actionApplicationResourceError](./actionapplicationresourceerror.md)
  An error that indicates an app required by the action is not found.
- [AMError.Code.actionApplicationVersionResourceError](./actionapplicationversionresourceerror.md)
  An error that indicates an app required by the action is the wrong version.
- [AMError.Code.actionArchitectureMismatchError](./actionarchitecturemismatcherror.md)
  An error that indicates the action’s binary is not compatible with the current processor.
- [AMError.Code.actionExceptionError](./actionexceptionerror.md)
  An error that indicates an action encounters an exception while running.
- [AMError.Code.actionExecutionError](./actionexecutionerror.md)
  An error that indicates an action encounters an error while running (reason unknown).
- [AMError.Code.actionFailedGatekeeperError](./actionfailedgatekeepererror.md)
  An error that indicates the action doesn’t meet the Gatekeeper security policy.
- [AMError.Code.actionFileResourceError](./actionfileresourceerror.md)
  An error that indicates a file required by the action is not found.
- [AMError.Code.actionInitializationError](./actioninitializationerror.md)
  An error that indicates Automator is unable to initialize an action (reason unknown).
- [AMError.Code.actionInsufficientDataError](./actioninsufficientdataerror.md)
  An error that indicates the action requires input data to run, but none was supplied.
- [AMError.Code.actionIsDeprecatedError](./actionisdeprecatederror.md)
  An error that indicates the action has been deprecated.
- [AMError.Code.actionLicenseResourceError](./actionlicenseresourceerror.md)
  An error that indicates a license required by the action was not found.
- [AMError.Code.actionLinkError](./actionlinkerror.md)
  An error that indicates the action’s executable failed to load due to linking issues.
- [AMError.Code.actionLoadError](./actionloaderror.md)
  An error that indicates the action’s executable failed to load.
- [AMError.Code.actionMalwareError](./actionmalwareerror.md)
  An error that indicates the action has been identified as malware by XProtect.
- [AMError.Code.actionNotLoadableError](./actionnotloadableerror.md)
  An error that indicates the action’s executable is of a type that is not loadable in the current process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amerror/code/actionruntimemismatcherror)*