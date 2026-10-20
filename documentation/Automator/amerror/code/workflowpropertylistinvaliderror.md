# AMError.Code.workflowPropertyListInvalidError

**Framework**: Automator  
**Kind**: case  
**Role**: Case

An error that indicates an attempt to open a workflow document whose property list couldn’t be read.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
case workflowPropertyListInvalidError
```

```c
AMWorkflowPropertyListInvalidError
```

#### Discussion

The property list document (`document.wflow`) could be missing, damaged, or constructed improperly.

## See Also

### Workflow Errors
- [AMError.Code.workflowActionsNotLoadedError](./workflowactionsnotloadederror.md)
  An error that indicates one of the actions of the workflow couldn’t be loaded.
- [AMError.Code.workflowNewerActionVersionError](./workflowneweractionversionerror.md)
  An error that indicates an action in a workflow is newer than the installed action.
- [AMError.Code.workflowNewerVersionError](./workflownewerversionerror.md)
  An error that indicates an attempt to open a workflow document that was saved with a newer version of Automator.
- [AMError.Code.workflowNoEnabledActionsError](./workflownoenabledactionserror.md)
  An error that indicates there are no enabled actions in the workflow.
- [AMError.Code.workflowOlderActionVersionError](./workflowolderactionversionerror.md)
  An error that indicates an action in a workflow is older than the installed action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amerror/code/workflowpropertylistinvaliderror)*