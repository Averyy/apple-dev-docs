# AMError.Code.workflowOlderActionVersionError

**Framework**: Automator  
**Kind**: case

An error that indicates an action in a workflow is older than the installed action.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
case workflowOlderActionVersionError
```

#### Discussion

This error is presented to the user as a warning.

## See Also

- [AMError.Code.workflowActionsNotLoadedError](amerror/code/workflowactionsnotloadederror.md)
  An error that indicates one of the actions of the workflow couldn’t be loaded.
- [AMError.Code.workflowNewerActionVersionError](amerror/code/workflowneweractionversionerror.md)
  An error that indicates an action in a workflow is newer than the installed action.
- [AMError.Code.workflowNewerVersionError](amerror/code/workflownewerversionerror.md)
  An error that indicates an attempt to open a workflow document that was saved with a newer version of Automator.
- [AMError.Code.workflowNoEnabledActionsError](amerror/code/workflownoenabledactionserror.md)
  An error that indicates there are no enabled actions in the workflow.
- [AMError.Code.workflowPropertyListInvalidError](amerror/code/workflowpropertylistinvaliderror.md)
  An error that indicates an attempt to open a workflow document whose property list couldn’t be read.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amerror/code/workflowolderactionversionerror)*